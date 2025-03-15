class Prompts:
    WELCOME = "Welcome to Auto Driving Car Simulation!\n"
    ENTER_WIDTH_HEIGHT = "Please enter the width and height of the simulation field in x y format\n"
    INVALID_FIELD_SIZE = "The format is incorrect. Please enter the width and height of the simulation field in x y format(x and y are two integers separated by one space):\n"
    ENTER_CAR_NAME = "Please enter the name of the car:\n"
    WRONG_CAR_NAME_FORMAT = "Wrong car name format. Please enter the name of the car with only letters:\n"
    SAME_CAR_NAME = "The car name already exists. Please enter a different name:\n"
    WRONG_CAR_POSITION_DIRECTION_FORMAT = "The format is incorrect. Please enter the position and direction of the car in x y direction format(no empty character in front and end and only one space for each separation):\n"
    SAME_CAR_POSITION = "The car position already occupied. Please enter the position and direction again:\n"
    OUT_OF_FIELD = "The car position is out of the field. Please enter the position and direction again:\n"
    INVALID_COMMANDS = "The command is invalid. Please enter the command for the car with only L, R, F:\n"
    ADD_SIMU_OPTIONS = "Please choose from the following options:\n[1] Add a car to field\n[2] Run simulation\n"
    INVALID_CHOICE = "Please key in '1' or '2' to choose from options.\n"
    RESTART_EXIT_OPTIONS = "Please choose from the following options:\n[1] Start over\n[2] Exit\n"
    @staticmethod
    def field_created(w, h):
        return f"You have created a field of {w} x {h}.\n"

    @staticmethod
    def enter_car_position_direction(car_name):
        return f"Please enter initial position of car {car_name} in x y Direction format:\n"
    @staticmethod
    def enter_car_commands(car_name):
        return f"Please enter the commands for car {car_name}:\n"
    @staticmethod
    def list_of_cars(car_ls):
        car_ls_str = "Your current list of cars are:\n"
        for car in car_ls:
            car_name, x, y, direction, command = car
            car_ls_str += f"- {car_name}, ({x},{y}) {direction}, {command}\n"
        return car_ls_str
    @staticmethod
    def list_of_cars_after_simulation(car_ls):
        car_ls_str = "After simulation, the result is:\n"
        for car in car_ls:
            car_name, x, y, direction, command = car
            car_ls_str += f"- {car_name}, ({x},{y}) {direction}\n"
        return car_ls_str
    @staticmethod
    def list_of_collisions(collision_record, car_ls):
        collision_ls_str = "After simulation, the result is:\n"
        car_order = {car[0]: i for i, car in enumerate(car_ls)}
        sorted_collision_keys = sorted(collision_record.keys(), key=lambda key: car_order.get(key[0], float('inf')))
        for position_step in sorted_collision_keys:
            car_name, x, y, step = position_step
            collided_car_name_ls = collision_record[position_step]
            collided_car_name_ls.sort(key=lambda car: car_order.get(car, float('inf')))
            collided_car_str = ", ".join(collided_car_name_ls)
            collision_ls_str += f"- {car_name}, collides with {collided_car_str} at ({x},{y}) at step {step}\n"
        return collision_ls_str
