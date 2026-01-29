# Use @pytest.mark.parametrize to test multiple input combinations

import pytest

@pytest.mark.parametrize(
    "a,b,result",
    [(2,3,5),
    (4,5,9),
     (1,5,6),
     ]
)
def test_add(a, b, result):
    assert a+b == result