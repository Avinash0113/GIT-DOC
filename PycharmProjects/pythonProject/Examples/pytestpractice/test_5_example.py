import pytest

def test_1():
    assert "avinash"=="avinash"
@pytest.mark.skip
def test_2():
    name="avinash"
    assert name.upper=="AVINASH"
@pytest.mark.xfail
def test_3():
    assert 1>10

def test_4():
    assert 5<1


def test_5():
    a=10
    b=20
    assert a==b
    assert a!=b

def test_6():
    assert 100>=100
@pytest.mark.xfail
def test_7():
    assert 50>10


