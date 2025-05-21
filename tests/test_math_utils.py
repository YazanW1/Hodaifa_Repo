import importlib.util
import os

# Dynamically load math_utils.py
script_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
module_path = os.path.join(script_dir, "math_utils.py")

spec = importlib.util.spec_from_file_location("math_utils", module_path)
math_utils = importlib.util.module_from_spec(spec)
spec.loader.exec_module(math_utils)

def test_add():
    assert math_utils.add(3, 4) == 7
    assert math_utils.add(-2, 5) == 3

def test_divide():
    assert math_utils.divide(10, 2) == 5
    assert math_utils.divide(5, 1) == 5

def test_divide_by_zero():
    try:
        math_utils.divide(5, 0)
        assert False  # should not reach here
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"