import pytest

# @pytest.mark
def test_a1():
    assert "house"=="home"
@pytest.mark.user
def test_a2():
    assert "bike"=="bike"

def test_a3():
    vehicle="car"
    assert vehicle.upper=="CAR"
@pytest.mark.user
def test_a4():
    a=5
    b=5
    assert a==b

def test_a5():
    a=5
    b=6
    assert a==b
@pytest.mark.user
def test_a6():
    assert 50>20
@pytest.mark.user
def test_a7():
    assert 50>100





