import pytest


def test_A1():
    assert True


def test_A2():
    assert False


def test_A3():
    a,b=5,4
    assert a==b


def test_A4():
    a,b=10,50
    c=a+b
    assert a==c


def test_A5():
    a,b=15,32
    c=a+b
    assert c==a+b


def test_A6():
    name="Python"
    assert name.upper()=="Python"


def test_A7():
    a=0
    assert a==True

@pytest.mark.skip
def test_A8():
    b=1
    assert b==False

@pytest.mark.xfail
def test_A9():
    a, b = 56, 4
    assert a == 52

@pytest.mark.check
def test_A10():
    a, b = 121, 510
    c = a + b
    assert a != c

@pytest.mark.user
def test_A11():
    true,false=1,0
    assert true==1


def test_A12():
    name = "PYTHON"
    assert name.upper() == "PYTHON"

@pytest.mark.xfail
def test_A13():
    name = "python"
    assert name.upper() == "python"


