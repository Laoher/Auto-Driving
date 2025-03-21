import pytest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))
from src.drive import Drive


@pytest.fixture(scope="function")
def drive():
    return Drive()
