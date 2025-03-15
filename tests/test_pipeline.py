import io

def test_pipeline_simple(drive, monkeypatch, capsys):
    # Simulate user input
    inputs = "10 20\nA\n1 1 N\nF\n2\n2"  # Valid input (note the newline)
    simulated_input = io.StringIO(inputs)
    monkeypatch.setattr("sys.stdin", simulated_input)

    # Call the method
    drive.run_pipeline()
    # Verify the result
    assert drive.width == 10
    assert drive.height == 20
    assert drive.car_ls == [("A", 1, 2, "N", "")]
    assert drive.collision_record == {}
    assert drive.moved_car_ls == ["A"]

    # Capture and verify the output
    captured = capsys.readouterr()
    expected_output = (
        'Welcome to Auto Driving Car Simulation!\n'
        'Please enter the width and height of the simulation field in x y format\n'
        'You have created a field of 10 x 20.\n\n'
        'Please enter the name of the car:\n'
        'Please enter initial position of car A in x y Direction format:\n'
        'Please enter the commands for car A:\n'
        'Your current list of cars are:\n'
        '- A, (1,1) N, F\n\n'
        'Please choose from the following options:\n'
        '[1] Add a car to field\n'
        '[2] Run simulation\n'
        'Your current list of cars are:\n'
        '- A, (1,1) N, F\n\n'
        'After simulation, the result is:\n'
        '- A, (1,2) N\n\n'
        'Please choose from the following options:\n'
        '[1] Start over\n'
        '[2] Exit\n'
    )
    assert captured.out == expected_output

def test_pipeline_complicated(drive, monkeypatch, capsys):
    # Simulate user input
    inputs = "0 0\n10 20\n1\nA\n-1 1 N\n1 1 N\nX\nF\n1\nA\nB\n1 1 S\n1 2 S\nF\n2\n1\n5 5\nB\n1 1 N\nF\n2\n2"  # Valid input (note the newline)
    simulated_input = io.StringIO(inputs)
    monkeypatch.setattr("sys.stdin", simulated_input)

    # Call the method
    drive.run_pipeline()
    # Verify the result
    assert drive.width == 5
    assert drive.height == 5
    assert drive.car_ls == [("B", 1, 2, "N", "")]
    assert drive.collision_record == {}
    assert drive.moved_car_ls == ["B"]

    # Capture and verify the output
    captured = capsys.readouterr()
    expected_output = (
        'Welcome to Auto Driving Car Simulation!\n'
        'Please enter the width and height of the simulation field in x y format\n'
        'The format is incorrect. Please enter the width and height of the simulation '
        'field in x y format(x and y are two integers separated by one space):\n'
        'You have created a field of 10 x 20.\n'
        '\n'
        'Please enter the name of the car:\n'
        'Wrong car name format. Please enter the name of the car with only letters:\n'
        'Please enter initial position of car A in x y Direction format:\n'
        'The format is incorrect. Please enter the position and direction of the car '
        'in x y direction format(no empty character in front and end and only one '
        'space for each separation):\n'
        'Please enter the commands for car A:\n'
        'The command is invalid. Please enter the command for the car with only L, R, '
        'F:\n'
        'Your current list of cars are:\n'
        '- A, (1,1) N, F\n'
        '\n'
        'Please choose from the following options:\n'
        '[1] Add a car to field\n'
        '[2] Run simulation\n'
        'Please enter the name of the car:\n'
        'The car name already exists. Please enter a different name:\n'
        'Please enter initial position of car B in x y Direction format:\n'
        'The car position already occupied. Please enter the position and direction '
        'again:\n'
        'Please enter the commands for car B:\n'
        'Your current list of cars are:\n'
        '- A, (1,1) N, F\n'
        '- B, (1,2) S, F\n'
        '\n'
        'Please choose from the following options:\n'
        '[1] Add a car to field\n'
        '[2] Run simulation\n'
        'Your current list of cars are:\n'
        '- A, (1,1) N, F\n'
        '- B, (1,2) S, F\n'
        '\n'
        'After simulation, the result is:\n'
        '- A, collides with B at (1,1) at step 1\n'
        '- B, collides with A at (1,2) at step 1\n'
        '\n'
        'Please choose from the following options:\n'
        '[1] Start over\n'
        '[2] Exit\n'
        'Welcome to Auto Driving Car Simulation!\n'
        'Please enter the width and height of the simulation field in x y format\n'
        'You have created a field of 5 x 5.\n'
        '\n'
        'Please enter the name of the car:\n'
        'Please enter initial position of car B in x y Direction format:\n'
        'Please enter the commands for car B:\n'
        'Your current list of cars are:\n'
        '- B, (1,1) N, F\n'
        '\n'
        'Please choose from the following options:\n'
        '[1] Add a car to field\n'
        '[2] Run simulation\n'
        'Your current list of cars are:\n'
        '- B, (1,1) N, F\n'
        '\n'
        'After simulation, the result is:\n'
        '- B, (1,2) N\n'
        '\n'
        'Please choose from the following options:\n'
        '[1] Start over\n'
        '[2] Exit\n'
    )
    assert captured.out == expected_output
