import pytest

@pytest.mark.skip(reason="Feature not implemented yet")
def test_skip_example():
    assert 1 == 0


@pytest.mark.xfail(reason="Known bug")
def test_xfail_example():
    assert 2 * 2 == 5
