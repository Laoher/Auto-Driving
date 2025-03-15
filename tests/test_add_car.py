import io
def test_add_car_valid_input(drive, monkeypatch, capsys):
    # Simulate user input
    inputs = "A\n1 1 N\nLFRF\n"  # Valid input
    simulated_input = io.StringIO(inputs)
    monkeypatch.setattr("sys.stdin", simulated_input)

    # Call the method
    drive.width = 5
    drive.height = 8
    drive.add_a_car()

    # Verify the result
    assert drive.car_ls == [("A", 1, 1, "N", "LFRF")]

    # Capture and verify the output
    captured = capsys.readouterr()
    expected_output = (
        "Please enter the name of the car:\n"
        "Please enter initial position of car A in x y Direction format:\n"
        "Please enter the commands for car A:\n"
        "Your current list of cars are:\n"
        "- A, (1,1) N, LFRF\n\n"
    )
    assert captured.out == expected_output

def test_add_car_invalid_duplicated_input(drive, monkeypatch, capsys):
    # Simulate user input (first valid, then invalid)
    inputs = "A\nB\n1 1 S\n1 2 N\nLFX\nLF\n"  # First valid, then invalid
    simulated_input = io.StringIO(inputs)
    monkeypatch.setattr("sys.stdin", simulated_input)

    # Call the method
    drive.width = 10
    drive.height = 20
    drive.car_ls = [("A", 1, 1, "N", "LF")]
    drive.add_a_car()

    # Verify the result
    assert drive.car_ls == [("A", 1, 1, "N", "LF"), ("B", 1, 2, "N", "LF")]

    # Capture and verify the output
    captured = capsys.readouterr()
    expected_output = (
        "Please enter the name of the car:\n"
        "The car name already exists. Please enter a different name:\n"
        "Please enter initial position of car B in x y Direction format:\n"
        "The car position already occupied. Please enter the position and direction again:\n"
        "Please enter the commands for car B:\n"
        "The command is invalid. Please enter the command for the car with only L, R, F:\n"
        "Your current list of cars are:\n"
        "- A, (1,1) N, LF\n"
        "- B, (1,2) N, LF\n\n"
    )
    assert captured.out == expected_output

def test_add_car_invalid_then_valid_input(drive, monkeypatch, capsys):
    # Simulate user input (first invalid, then valid)
    inputs = "123\nA\n1 1\n1 1 N\nLFX\nLFRF\n"  # First invalid, then valid
    simulated_input = io.StringIO(inputs)
    monkeypatch.setattr("sys.stdin", simulated_input)

    # Call the method
    drive.width = 7
    drive.height = 7
    drive.add_a_car()

    # Verify the result
    assert drive.car_ls == [("A", 1, 1, "N", "LFRF")]

    # Capture and verify the output
    captured = capsys.readouterr()
    expected_output = (
        "Please enter the name of the car:\n"
        "Wrong car name format. Please enter the name of the car with only letters:\n"
        "Please enter initial position of car A in x y Direction format:\n"
        "The format is incorrect. Please enter the position and direction of the car in x y direction format(no empty character in front and end and only one space for each separation):\n"
        "Please enter the commands for car A:\n"
        "The command is invalid. Please enter the command for the car with only L, R, F:\n"
        "Your current list of cars are:\n"
        "- A, (1,1) N, LFRF\n\n"
    )
    assert captured.out == expected_output

def test_add_car_multiple_invalid_inputs(drive, monkeypatch, capsys):
    # Simulate user input (multiple invalid, then valid)
    inputs = "123\n1a\nA\n-1 1 N\n1 1\n1 1 N\n1x\nLFX\nLFRF\n"  # First two invalid, last valid
    simulated_input = io.StringIO(inputs)
    monkeypatch.setattr("sys.stdin", simulated_input)

    # Call the method
    drive.width = 10
    drive.height = 20
    drive.add_a_car()

    # Verify the result
    assert drive.car_ls == [("A", 1, 1, "N", "LFRF")]

    # Capture and verify the output
    captured = capsys.readouterr()
    expected_output = (
        "Please enter the name of the car:\n"
        "Wrong car name format. Please enter the name of the car with only letters:\n"
        "Wrong car name format. Please enter the name of the car with only letters:\n"
        "Please enter initial position of car A in x y Direction format:\n"
        "The format is incorrect. Please enter the position and direction of the car in x y direction format(no empty character in front and end and only one space for each separation):\n"
        "The format is incorrect. Please enter the position and direction of the car in x y direction format(no empty character in front and end and only one space for each separation):\n"
        "Please enter the commands for car A:\n"
        "The command is invalid. Please enter the command for the car with only L, R, F:\n"
        "The command is invalid. Please enter the command for the car with only L, R, F:\n"
        "Your current list of cars are:\n"
        "- A, (1,1) N, LFRF\n"
        "\n"

    )
    assert captured.out == expected_output