# Auto-Driving

GIC assignment solution

# Assumptions

1. Additional and unnecessary space or empty string is not allowed for any input ,so the user needs to strictly follow
   the format in the assignment description
2. The system will ask the user to add a car before showing the choices of adding a car or running simulation
3. Car name format
    - Each car name must be unique
    - Can only be composed of upper case and lower case letters
4. Position format
    - Each initial position must be unique;
    - Since the position is unique, the number of cars will not larger than the number of grids
5. Command
    - Only the capital letters of 'F', 'L', 'R' are allowed
6. Collision
    - Frontal collision: when two cars are going to collide face to face with distance of 1 grid
    - Lateral collision: any other collision except frontal collision
    - Collision point: the point where a car experiences a collision with another car.
    - Behavior of collided cars: The car will stop at the collision position, becoming an obstacle for other moving cars
      and potentially causing further collisions.
    - Behaviour of collided point: this collision point will become a shared position for the collided cars and can hold
      unlimited number of cars
    - How to define which position is the collision point: 
          The rules differ slightly between frontal and lateral collisions.
        - Frontal collision: the position before the collision is the collision point for each car
        - Lateral collision: the position where both/all the cars collided
    - In a frontal collision, both cars will stop at the position one step before the collision which is also the
      collision point for each car.
    - In a lateral collision, all cars with forward command will continue to go to the new position which is the
      collision position for all the cars collided at this position in that step
    - In the final collision report, for a certain car, only the cars it collided with in its first collision will be
      shown. Further collisions in the following steps with the same car will not be shown in the same line of the
      report

# How to run the program

## Clone the repository: Open a terminal, navigate to your desired directory, and run:

``` bash
git clone https://github.com/Laoher/Auto-Driving.git
```

## Prepare the environment:

Make sure Python 3 and Pipenv are installed.

``` bash
python3 -m pip install --user pipenv
```

``` bash
cd Auto-Driving
pipenv shell
pipenv install
```

## Run the program

``` bash
python src/drive.py
```

And then follow the instructions to add cars and run the simulation

## Run the tests

``` bash
pytest tests
```

# Potential Improvements

There are several improvements that can be made to the current implementation:

1. Add GUI to simulate the process
2. Use arrow key to select from options
3. Command like 'exit' can be used to end the program at any time