import pytest

@pytest.mark.parametrize("input_str, expected", [
    ("5 5", (True, "PASS")),
    ("10 20", (True, "PASS")),
    ("123 456", (True, "PASS")),
    ("99999 1", (True, "PASS")),
    ("0 0", (False, "INVALID_FIELD_SIZE")),  # 0 is not allowed
    ("0 20", (False, "INVALID_FIELD_SIZE")),  # 0 is not allowed
    ("20 0 ", (False, "INVALID_FIELD_SIZE")),  # 0 is not allowed
    ("10,20", (False, "INVALID_FIELD_SIZE")),  # no comma
    ("10  20", (False, "INVALID_FIELD_SIZE")),  # multiple spaces
    ("01 20", (False, "INVALID_FIELD_SIZE")),  # 01 is not valid integer format
    ("10 020", (False, "INVALID_FIELD_SIZE")),  # 020 is not valid integer format
    ("10 ", (False, "INVALID_FIELD_SIZE")),  # missing y
    (" 10 20", (False, "INVALID_FIELD_SIZE")),  # leading space
    ("10 20!", (False, "INVALID_FIELD_SIZE")),  # special character
    ("abc 10", (False, "INVALID_FIELD_SIZE")),  # not integer
])
def test_is_valid_field_size(drive, input_str, expected):
    assert drive.is_valid_field_size(input_str) == expected

@pytest.mark.parametrize("input_str, expected", [
    ("Car", (True, "PASS")),
    ("abc", (True, "PASS")),
    ("ABC", (True, "PASS")),
    ("a", (True, "PASS")),
    ("A", (True, "PASS")),
    ("Aa", (True, "PASS")),
    ("A ", (False, "WRONG_CAR_NAME_FORMAT")),  # trailing space
    ("a b", (False, "WRONG_CAR_NAME_FORMAT")),  # space
    ("a!", (False, "WRONG_CAR_NAME_FORMAT")),  # special character
    ("CarA", (False, "SAME_CAR_NAME")),  # already exists
    ("C_a", (False, "WRONG_CAR_NAME_FORMAT")),  # special character
    ("", (False, "WRONG_CAR_NAME_FORMAT")),  # empty
])
def test_is_valid_car_name(drive, input_str, expected):
    drive.car_ls = [('CarA', 1, 2, 'N', 'LFRF'), ('CarB', 3, 3, 'E', 'FRFL')]
    assert drive.is_valid_car_name(input_str) == expected

@pytest.mark.parametrize("input_str, expected", [
    ("1 1 W", (True, 'PASS')),
    ("0 0 W", (True, 'PASS')),
    ("4 3 N", (True, 'PASS')),
    ("5 4 N", (False, 'OUT_OF_FIELD')),  # out of field
    ("10 20N", (False, 'WRONG_CAR_POSITION_DIRECTION_FORMAT')),  # no space
    ("10  20 N", (False, 'WRONG_CAR_POSITION_DIRECTION_FORMAT')),  # multiple spaces
    ("-1 5 E", (False, 'WRONG_CAR_POSITION_DIRECTION_FORMAT')),  # negative number
    ("10 20 X", (False, 'WRONG_CAR_POSITION_DIRECTION_FORMAT')),  # wrong direction format
    ("10 20", (False, 'WRONG_CAR_POSITION_DIRECTION_FORMAT')),  # no direction
])
def test_is_valid_car_position_direction(drive, input_str, expected):
    drive.width = 5
    drive.height = 5
    assert drive.is_valid_car_position_direction(input_str) == expected

@pytest.mark.parametrize("input_str, expected", [
    ("LFRF", (True, 'PASS')),
    ("L", (True, 'PASS')),
    ("R", (True, 'PASS')),
    ("F", (True, 'PASS')),
    ("LFRF ", (False, 'INVALID_COMMANDS')),  # trailing space
    ("LFRF!", (False, 'INVALID_COMMANDS')),  # special character
    ("LFRF1", (False, 'INVALID_COMMANDS')),  # number
    ("LF RF", (False, 'INVALID_COMMANDS')),  # space
    ("LX ", (False, 'INVALID_COMMANDS')),  # wrong command
    ("", (False, 'INVALID_COMMANDS')),  # empty
])
def test_is_valid_commands(drive, input_str, expected):
    assert drive.is_valid_commands(input_str) == expected
