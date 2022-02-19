import pytest

def test_1():
    a=3
    b=4
    assert a+1==b
    assert a==b

def test_2():
    name="avinash"
    assert name.upper()=="AVINASH"

def test_3():
    assert False

def test_4():
    assert True

def test_5():
    assert "avinash"=="avinash"

def test_6():
    assert 10==100
@pytest.mark.user
def test_7():
    assert "admin"=="admin"


def test_A10():
    a, b = 12, 50
    c = a + b
    assert a != c


def test_A11():
    true,false=0,0
    assert true==0
