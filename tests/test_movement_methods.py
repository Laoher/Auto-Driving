import pytest
from src.drive import Drive

@pytest.mark.parametrize("direction, expected", [
    ("N", "E"),
    ("E", "S"),
    ("S", "W"),
    ("W", "N"),
])
def test_turn_right(direction, expected):
    assert Drive.turn_right(direction) == expected

@pytest.mark.parametrize("direction, expected", [
    ("N", "W"),
    ("W", "S"),
    ("S", "E"),
    ("E", "N"),
])
def test_turn_left(direction, expected):
    assert Drive.turn_left(direction) == expected

@pytest.mark.parametrize("x, y, direction, expected", [
    (1, 1, "N", (1, 2)),
    (1, 1, "W", (0, 1)),
    (1, 1, "S", (1, 0)),
    (1, 1, "E", (2, 1)),
    (0, 0, "N", (0, 1)),
    (0, 0, "W", (0, 0)),
    (0, 0, "S", (0, 0)),
    (0, 0, "E", (1, 0)),
    (4, 4, "N", (4, 4)),
    (4, 4, "W", (3, 4)),
    (4, 4, "S", (4, 3)),
    (4, 4, "E", (4, 4)),
])
def test_move_forward(x, y, direction, expected, drive):
    drive.width = 5
    drive.height = 5
    assert drive.move_forward(x, y, direction) == expected
