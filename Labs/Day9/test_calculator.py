import pytest

# =========================================================
# 2. Use a Python unit testing framework (pytest)
# =========================================================
# Pytest is used here to write and run unit test cases.
# Test functions start with `test_` and use `assert`.


def test_addition():
    assert add(2, 3) == 5


def test_subtraction():
    assert subtract(5, 3) == 2


def test_multiplication():
    assert multiply(4, 3) == 12


def test_division():
    assert divide(10, 2) == 5


def test_division_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


# =========================================================
# 3. Implement the calculator functions to make tests pass
# =========================================================
# These functions are written AFTER the tests,
# following the Test Driven Development approach.


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


# =========================================================
# 4. Demonstrate handling of edge cases (division by zero)
# =========================================================
# The divide function checks for division by zero
# and raises a ValueError to prevent runtime errors.


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


# =========================================================
# 5. TDD Cycle: Red → Green → Refactor
# =========================================================


"""
RED:
- Test cases are written first (above).
- Initially, tests fail because functions do not exist.

GREEN:
- Calculator functions are implemented.
- All tests pass successfully.

REFACTOR:
- Code can be improved (for readability, validation, reuse)
- without changing functionality.
- Tests ensure behavior remains correct.
"""
