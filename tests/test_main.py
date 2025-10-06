import sys
import os
from src.main import add

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_add():
    assert add(2, 3) == 5
