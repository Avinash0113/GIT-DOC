import pytest


def test_add():
    result = 10
    assert 10 + 20 == result

def test_sub():
    result = 20
    assert 30-10 == result

def test_mul():
    result = 30
    assert 10 * 4 == result

def test_mod():
    result = 0
    assert 10 % 2 == result

def test_div():
    result = 3
    assert 10 //3 == result