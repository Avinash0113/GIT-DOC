import pytest

def test_a():
    assert 1<5
@pytest.mark.skip
def test_b():
    assert 5<=5
@pytest.mark.data
def test_c():
    assert 10>5

def test_d():
    assert 10<10
