import pytest

def test_total_divisibe_by_5(input_total):
    assert input_total % 5==0

#@pytest.fixture
def test_total_divisibe_by_10(input_total):
    assert input_total % 10==0

def test_total_divisibe_by_20(input_total):
    assert input_total % 20==0