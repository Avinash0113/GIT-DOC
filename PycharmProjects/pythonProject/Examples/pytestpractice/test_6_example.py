import pytest


@pytest.mark.parametrize("rollno,percentage", [(1485455,95),(2,36),(3,35),(4,24),(51,101)])
def test_student_pass(rollno,percentage):
   print(rollno,percentage)
   assert 1<=rollno<=1000
   assert 35<=percentage<=100