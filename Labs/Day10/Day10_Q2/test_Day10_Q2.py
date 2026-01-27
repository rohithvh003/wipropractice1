import pytest

# xUnit-style setup and teardown

def setup_module(module):
    print("\n[Setup Module]")

def teardown_module(module):
    print("\n[Teardown Module]")

def setup_function(function):
    print("\n[Setup Function]")

def teardown_function(function):
    print("\n[Teardown Function]")


# Application code

def add(a, b):
    return a + b

def reverse_string(text):
    return text[::-1]


# Tests USING fixtures from conftest.py

def test_addition(numbers):
    a, b = numbers
    assert add(a, b) == 15


def test_reverse_string(sample_text):
    assert reverse_string(sample_text) == "tsetyp"
