import pytest
import time

def test_1():
    result = 10
    assert 10 + 20 == result

def test_2():
    result = 20
    assert 30-10 == result

@pytest.mark.order(1)
def test_3():
    result = 40
    assert 10 * 4 == result

def test_4():
    result = 0
    assert 10 % 2 == result

