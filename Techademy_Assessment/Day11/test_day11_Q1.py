import pytest


def apply_tax(amount, rate):
    return amount * rate

# Parametrized test
@pytest.mark.parametrize(
    "amount,rate,expected",
    [
        (100, 0.2, 20),
        (200, 0.2, 40),
        (0, 0.3, 0),
    ]
)
def test_tax_calculation(amount, rate, expected):
    assert apply_tax(amount, rate) == expected

# Skip test
@pytest.mark.skip(reason="Feature need to develope")
def test_skip_example():
    assert apply_tax(100, 0.2) == 20



# XFail test
@pytest.mark.xfail(reason="rounding issue")
def test_xfail_example():
    assert apply_tax(99, 0.15) == 14.85



# Using command-line option
def test_country(country):
    assert country in ["INDIA", "US", "UK"]
