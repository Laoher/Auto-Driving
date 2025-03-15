def test_run_simulation_no_collision(drive, monkeypatch, capsys):
    drive.width = 10
    drive.height = 20
    drive.car_ls = [("A", 1, 1, "N", "LFRF"), ("B", 2, 2, "E", "LFRF")]
    drive.run_simulation()

    # Capture and verify the output
    captured = capsys.readouterr()
    expected_output = (
        "Your current list of cars are:\n"
        "- A, (1,1) N, LFRF\n"
        "- B, (2,2) E, LFRF\n"
        "\n"
        "After simulation, the result is:\n"
        "- A, (0,2) N\n"
        "- B, (3,3) E\n"
        "\n"
    )
    assert captured.out == expected_output

def test_run_simulation_with_single_collision(drive, monkeypatch, capsys):
    drive.width = 10
    drive.height = 20
    drive.car_ls = [("A", 1, 1, "N", "F"), ("B", 1, 3, "S", "F"), ("C", 5, 1, "W", "F"), ("D", 8, 8, "E", "F"), ]
    drive.run_simulation()

    # Capture and verify the output
    captured = capsys.readouterr()
    expected_output = (
        'Your current list of cars are:\n'
        '- A, (1,1) N, F\n'
        '- B, (1,3) S, F\n'
        '- C, (5,1) W, F\n'
        '- D, (8,8) E, F\n'
        '\n'
        'After simulation, the result is:\n'
        '- A, collides with B at (1,2) at step 1\n'
        '- B, collides with A at (1,2) at step 1\n'
        '\n'
    )
    assert captured.out == expected_output

def test_run_simulation_with_multiple_collision(drive, monkeypatch, capsys):
    drive.width = 10
    drive.height = 20
    drive.car_ls = [("A", 1, 1, "N", "F"), ("B", 1, 2, "S", "F"), ("C", 2, 1, "W", "F"), ("D", 0, 1, "E", "F"),
                    ("E", 1, 0, "N", "F"), ("F", 3, 1, "W", "FF"), ("G", 1, 3, "S", "F"), ("H", 1, 4, "S", "FF"),
                    ("I", 5, 5, "S", "F")]
    drive.run_simulation()

    # Capture and verify the output
    captured = capsys.readouterr()
    expected_output = (
        'Your current list of cars are:\n'
        '- A, (1,1) N, F\n'
        '- B, (1,2) S, F\n'
        '- C, (2,1) W, F\n'
        '- D, (0,1) E, F\n'
        '- E, (1,0) N, F\n'
        '- F, (3,1) W, FF\n'
        '- G, (1,3) S, F\n'
        '- H, (1,4) S, FF\n'
        '- I, (5,5) S, F\n'
        '\n'
        'After simulation, the result is:\n'
        '- A, collides with B, C, D, E at (1,1) at step 1\n'
        '- B, collides with A, G at (1,2) at step 1\n'
        '- C, collides with A, D, E at (1,1) at step 1\n'
        '- D, collides with A, C, E at (1,1) at step 1\n'
        '- E, collides with A, C, D at (1,1) at step 1\n'
        '- F, collides with A, C, D, E at (1,1) at step 2\n'
        '- G, collides with B at (1,2) at step 1\n'
        '- H, collides with B, G at (1,2) at step 2\n'
        '\n'
    )
    assert captured.out == expected_output

def test_run_simulation_with_fully_occupied_field(drive, monkeypatch, capsys):
    drive.width = 2
    drive.height = 2
    drive.car_ls = [("A", 0, 0, "N", "F"), ("B", 0, 1, "S", "F"), ("C", 1, 0, "W", "F"), ("D", 1, 1, "E", "F")]
    drive.run_simulation()

    # Capture and verify the output
    captured = capsys.readouterr()
    expected_output = (
        'Your current list of cars are:\n'
        '- A, (0,0) N, F\n'
        '- B, (0,1) S, F\n'
        '- C, (1,0) W, F\n'
        '- D, (1,1) E, F\n'
        '\n'
        'After simulation, the result is:\n'
        '- A, collides with B, C at (0,0) at step 1\n'
        '- B, collides with A at (0,1) at step 1\n'
        '- C, collides with A at (0,0) at step 1\n'
        '\n'
    )
    assert captured.out == expected_output
