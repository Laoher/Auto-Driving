import io

def test_create_field_valid_input(drive, monkeypatch, capsys):
    # Simulate user input
    inputs = "10 20\n"  # Valid input
    simulated_input = io.StringIO(inputs)
    monkeypatch.setattr("sys.stdin", simulated_input)

    # Call the method
    drive.create_field()

    # Verify the result
    assert drive.width == 10
    assert drive.height == 20

    # Capture and verify the output
    captured = capsys.readouterr()
    expected_output = (
        "Welcome to Auto Driving Car Simulation!\n"
        "Please enter the width and height of the simulation field in x y format\n"
        "You have created a field of 10 x 20.\n\n"
    )
    assert captured.out == expected_output

def test_create_field_invalid_then_valid_input(drive, monkeypatch, capsys):
    # Simulate user input (first invalid, then valid)
    inputs = "invalid\n10 20\n"  # First invalid, then valid
    simulated_input = io.StringIO(inputs)
    monkeypatch.setattr("sys.stdin", simulated_input)

    # Call the method
    drive.create_field()

    # Verify the result
    assert drive.width == 10
    assert drive.height == 20

    # Capture and verify the output
    captured = capsys.readouterr()
    expected_output = (
        "Welcome to Auto Driving Car Simulation!\n"
        "Please enter the width and height of the simulation field in x y format\n"
        "The format is incorrect. Please enter the width and height of the simulation field in x y format(x and y are two integers separated by one space):\n"
        "You have created a field of 10 x 20.\n\n"
    )
    assert captured.out == expected_output

def test_create_field_multiple_invalid_inputs(drive, monkeypatch, capsys):
    # Simulate user input (multiple invalid, then valid)
    inputs = "invalid\n0 0\n10 20\n"  # First two invalid, last valid
    simulated_input = io.StringIO(inputs)
    monkeypatch.setattr("sys.stdin", simulated_input)

    # Call the method
    drive.create_field()

    # Verify the result
    assert drive.width == 10
    assert drive.height == 20

    # Capture and verify the output
    captured = capsys.readouterr()
    expected_output = (
        "Welcome to Auto Driving Car Simulation!\n"
        "Please enter the width and height of the simulation field in x y format\n"
        "The format is incorrect. Please enter the width and height of the simulation field in x y format(x and y are two integers separated by one space):\n"
        "The format is incorrect. Please enter the width and height of the simulation field in x y format(x and y are two integers separated by one space):\n"
        "You have created a field of 10 x 20.\n\n"
    )
    assert captured.out == expected_output
