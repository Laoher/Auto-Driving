# Auto-Driving

GIC assignment solution

# Assumptions

1. Additional and unnecessary space or empty string in the input is not allowed, so the user needs to strictly follow
   the format in the assignment description
2. The system forces the user to add a car before showing the choices of adding a car or running simulation
3. Car name
    - can only be composed of letters;
4. Position
    - The initial position must be unique;
    - since the position is unique, the car number will not larger than the number of grids
5. Command
    - No empty initial command of cars is allowed
6. Collision
    - One position can hold unlimited number of cars
    - All collided cars will stop at the position of collision and become obstacles for other further moving cars and
       might cause further collisions
    - If a car is going to collide with another car face to face with distance of 1 grid, the car will stop at the
       position before the collision which is also the collision position for each car.
    - For any other collision, the car with forward command will continue to go to the new position which is the
       collision position for all the cars collided at this position in that step
    - In the collision report, for a certain car, only the cars it collided with in its first time of collision will be shown. Further
       collisions in the following steps with the same car will not be shown in the same line within its collision list.
    

# How to run the program
## Get the repo: go to terminal and the path for running and key in
``` bash
git clone https://github.com/Laoher/Auto-Driving.git
```
##  Prepare the environment: 
``` bash
cd Auto-Driving
pip install pipenv
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

# Improvements
There are several improvements that can be made to the current implementation:
1. Add GUI to simulate the process
2. Use arrow key to select the options
3. Command like 'exit' can be used to end the program at any time