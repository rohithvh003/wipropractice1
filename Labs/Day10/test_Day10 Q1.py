import pytest

# =========================================================
# Code under test
# =========================================================
# Q1. Write unit tests using Pytest conventions
# File name starts with test_
# Test functions start with test_


def reverse_string(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text[::-1]


# =========================================================
# 1. Unit tests using Pytest conventions
# (test_*.py and test_ functions)
# =========================================================

def test_reverse_string_basic():
    assert reverse_string("hello") == "olleh"


# =========================================================
# Use assert statements to validate results
# =========================================================
#
# Q3. Use assert statements to validate results
# Assertions compare actual output with expected output.

def test_reverse_string_with_spaces():
    assert reverse_string("hello world") == "dlrow olleh"


# =========================================================
# Test to validate exception is raised
# =========================================================
# Q4. Write a test to validate an exception
# pytest.raises() is used to verify exceptions.



def test_reverse_string_invalid_input():
    with pytest.raises(TypeError):
        reverse_string(123)
