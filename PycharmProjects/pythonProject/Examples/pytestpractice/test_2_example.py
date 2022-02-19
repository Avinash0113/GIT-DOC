import pytest

def test_m1():
    a=1
    b=3
    assert a+2==b
    assert a==b

def test_m2():
    assert 50==90

def test_m3():
    assert "PYTHON"=="PYTHON"

def test_m4():
    city="NELLORE"
    assert city.lower=="NELLORE"
@pytest.mark.user
def test_6():
    assert 10==100

def test_7():
    assert "admin"=="admin"
