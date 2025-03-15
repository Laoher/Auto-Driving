import dataclasses
import re
from collections import defaultdict
from typing import Optional, List, Dict, Tuple

from constants import Prompts

@dataclasses.dataclass
class Drive:
    width: Optional[int] = None
    height: Optional[int] = None
    car_ls: List[Tuple[str, int, int, str, str]] = dataclasses.field(default_factory=list)
    collision_record: Dict[Tuple[str, int, int, int], List[str]] = dataclasses.field(default_factory=dict)
    moved_car_ls: List[str] = dataclasses.field(default_factory=list)

    def reset(self) -> None:
        self.width = None
        self.height = None
        self.car_ls = []
        self.collision_record = {}
        self.moved_car_ls = []

    def create_field(self) -> None:
        field_size = input(Prompts.WELCOME + Prompts.ENTER_WIDTH_HEIGHT)
        is_valid_field_size = False
        while not is_valid_field_size:
            is_valid, message = self.is_valid_field_size(field_size)
            if not is_valid:
                field_size = input(Prompts.INVALID_FIELD_SIZE)
            else:
                is_valid_field_size = True


        self.width, self.height = [int(size) for size in field_size.split(" ")]
        print(Prompts.field_created(self.width, self.height))

    def add_a_car(self) -> None:
        # get car name
        car_name = input(Prompts.ENTER_CAR_NAME)
        is_valid_car_name = False
        while not is_valid_car_name:
            is_valid, message = self.is_valid_car_name(car_name)
            if is_valid:
                is_valid_car_name = True
            else:
                if message == "SAME_CAR_NAME":
                    car_name = input(Prompts.SAME_CAR_NAME)
                else:
                    car_name = input(Prompts.WRONG_CAR_NAME_FORMAT)
        # get car position and direction
        car_position_direction = input(Prompts.enter_car_position_direction(car_name))
        is_valid_car_position_direction = False
        while not is_valid_car_position_direction:
            is_valid, message = self.is_valid_car_position_direction(car_position_direction)
            if is_valid:
                is_valid_car_position_direction = True
            elif message == "SAME_CAR_POSITION":
                car_position_direction = input(Prompts.SAME_CAR_POSITION)
            elif message == "OUT_OF_FIELD":
                car_position_direction = input(Prompts.OUT_OF_FIELD)
            else:
                car_position_direction = input(Prompts.WRONG_CAR_POSITION_DIRECTION_FORMAT)
        x_str, y_str, direction = car_position_direction.split(" ")
        x, y = int(x_str), int(y_str)
        # get car commands
        command = input(Prompts.enter_car_commands(car_name))
        is_valid_command = False
        while not is_valid_command:
            is_valid, message = self.is_valid_commands(command)
            if is_valid:
                is_valid_command = True
            else:
                command = input(Prompts.INVALID_COMMANDS)
        self.car_ls.append((car_name, x, y, direction, command))
        print(Prompts.list_of_cars(self.car_ls))

    def run_simulation(self) -> None:
        print(Prompts.list_of_cars(self.car_ls))
        command_all_applied = False
        step = 0
        while not command_all_applied:
            step += 1
            self.moved_car_ls = []
            self.detect_frontal_collision(step)
            self.detect_lateral_collision(step)

            # check if all commands are applied
            all_command = ''.join([car[4] for car in self.car_ls])
            if len(all_command) == 0:
                command_all_applied = True
        if self.collision_record:
            print(Prompts.list_of_collisions(self.collision_record, self.car_ls))
        else:
            print(Prompts.list_of_cars_after_simulation(self.car_ls))

    def detect_frontal_collision(self, step):
        last_moves = [(car_name, x, y, direction, "" if len(command) == 0 else command[0]) for
                      car_name, x, y, direction, command in self.car_ls]
        for i, (car1, x1, y1, direction1, c1) in enumerate(last_moves):
            if c1 == "F":
                for j, (car2, x2, y2, direction2, c2) in enumerate(last_moves):
                    if i != j and c2 == "F":
                        if (x1 == x2 and y1 == y2 - 1 and direction1 == "N" and direction2 == "S") or \
                                (x1 == x2 and y1 == y2 + 1 and direction1 == "S" and direction2 == "N") or \
                                (x1 == x2 - 1 and y1 == y2 and direction1 == "E" and direction2 == "W") or \
                                (x1 == x2 + 1 and y1 == y2 and direction1 == "W" and direction2 == "E"):
                            self.collision_record[car1, x1, y1, step] = [car2]
                            self.collision_record[car2, x2, y2, step] = [car1]
                            # delete the remaining commands for the cars that has frontal collision
                            self.car_ls =[(item[0],item[1],item[2],item[3],"") if item[0] in [car1, car2] else item for item in self.car_ls ]
                            # record moved cars in this step
                            self.moved_car_ls.extend([car1, car2])

    def detect_lateral_collision(self, step: int) -> None:
        for i, (car_name, x, y, direction, command) in enumerate(self.car_ls):
            if len(command) == 0:
                continue
            # execute the command of this step for each car
            c = command[0]
            if c == "L":
                self.car_ls[i] = (car_name, x, y, self.turn_left(direction), command[1:])
            elif c == "R":
                self.car_ls[i] = (car_name, x, y, self.turn_right(direction), command[1:])
            elif c == "F":
                x, y = self.move_forward(x, y, direction)
                self.car_ls[i] = (car_name, x, y, direction, command[1:])
            # record moved cars in this step
            self.moved_car_ls.append(car_name)
        # record all the cars at one position
        position_map = defaultdict(list)
        for i, (car_name, x, y, direction, command) in enumerate(self.car_ls):
            position_map[(x, y)].append(car_name)
        # check if there are more than one car at the same position
        for position, car_names in position_map.items():
            x, y = position
            if len(car_names) > 1:
                for car_name in car_names:
                    if car_name in self.moved_car_ls:
                        # only record the collision happened in this step
                        other_car_names = [car for car in car_names if car != car_name]
                        self.collision_record[car_name, x, y, step] = self.collision_record.get(
                            (car_name, x, y, step), [])
                        for other_car_name in other_car_names:
                            self.collision_record[car_name, x, y, step].append(other_car_name)
                        self.car_ls =[(item[0],item[1],item[2],item[3],"") if item[0] == car_name else item for item in self.car_ls ]

    def run_pipeline(self) -> None:
        drive_finished = False
        while not drive_finished:
            self.reset()
            self.create_field()
            add_or_simu_choice = "1"
            while add_or_simu_choice == "1":
                self.add_a_car()
                add_or_simu_choice = self.get_add_or_simu_choice()
            self.run_simulation()
            restart_or_exit = self.get_restart_or_exit_choice()
            if restart_or_exit == "2":
                drive_finished = True

    @staticmethod
    def get_add_or_simu_choice() -> str:
        add_or_simu_choice = input(Prompts.ADD_SIMU_OPTIONS)
        while True:
            if add_or_simu_choice != "1" and add_or_simu_choice != "2":
                add_or_simu_choice = input(Prompts.INVALID_CHOICE)
            else:
                return add_or_simu_choice

    @staticmethod
    def get_restart_or_exit_choice() -> str:
        restart_or_exit = input(Prompts.RESTART_EXIT_OPTIONS)
        while True:
            if restart_or_exit != "1" and restart_or_exit != "2":
                restart_or_exit = input(Prompts.INVALID_CHOICE)
            else:
                return restart_or_exit

    @staticmethod
    def is_valid_field_size(input_str: str) -> Tuple[bool, str]:
        pattern = re.compile(r'^(?!0)\d+ (?!0)\d+$')
        if not bool(re.fullmatch(pattern, input_str)):
            return False, "INVALID_FIELD_SIZE"
        return True, "PASS"

    def is_valid_car_name(self, input_str: str) -> Tuple[bool, str]:
        if input_str in [car[0] for car in self.car_ls]:
            return False, "SAME_CAR_NAME"
        pattern = re.compile(r'^[a-zA-Z]+$')
        if not bool(re.fullmatch(pattern, input_str)):
            return False, "WRONG_CAR_NAME_FORMAT"
        return True, "PASS"

    def is_valid_car_position_direction(self, input_str: str) -> Tuple[bool, str]:
        if self.width is None or self.height is None:
            raise ValueError("Width and height must be initialized as integers.")
        pattern = re.compile(r'^(0|[1-9]\d*) (0|[1-9]\d*) [NESW]$')
        if not bool(re.fullmatch(pattern, input_str)):
            return False, "WRONG_CAR_POSITION_DIRECTION_FORMAT"
        x, y, direction = input_str.split(" ")
        position_ls = [(car[1], car[2]) for car in self.car_ls]
        if (int(x), int(y)) in position_ls:
            return False, "SAME_CAR_POSITION"
        if int(x) >= self.width or int(y) >= self.height:  # int x, y should be larger than 0 by limitation of regex
            return False, "OUT_OF_FIELD"
        return True, "PASS"

    @staticmethod
    def is_valid_commands(input_str: str) -> Tuple[bool, str]:
        pattern = re.compile(r'^[LRF]+$')
        if not bool(re.fullmatch(pattern, input_str)):
            return False, "INVALID_COMMANDS"
        return True, "PASS"

    @staticmethod
    def turn_left(direction: str) -> str:
        return {"N": "W", "W": "S", "S": "E", "E": "N"}[direction]

    @staticmethod
    def turn_right(direction: str) -> str:
        return {"N": "E", "E": "S", "S": "W", "W": "N"}[direction]

    def move_forward(self, x: int, y: int, direction: str) -> Tuple[int, int]:
        if self.width is None or self.height is None:
            raise ValueError("Width and height must be initialized as integers.")

        moves = {
            "N": (x, y + 1),
            "S": (x, y - 1),
            "E": (x + 1, y),
            "W": (x - 1, y)
        }
        new_x, new_y = moves[direction]
        return (new_x, new_y) if 0 <= new_x < self.width and 0 <= new_y < self.height else (x, y)

if "__main__" == __name__:
    drive = Drive()
    drive.run_pipeline()
