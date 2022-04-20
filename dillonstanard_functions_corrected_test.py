
import math
import pytest

## takes two numbers and returns
## the result of a division
def numbers(num1, num2):

    try:
        return num1 / num2
    except TypeError:
        print("Please enter a number.")

def test_numbers_1():
    assert numbers(4,2) == 2

def test_numbers_fail_1():
    assert numbers(4,2) == 10

def test_numbers_fail_2():
    assert numbers("x","b") == None

def test_numbers_2():
    assert numbers(22.5, 9) == 2.5

## takes in two points
## finds the distance between the points
def dist(x1, y1, x2, y2):

    try:
        dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
        dist = math.sqrt(dist)

        return dist
    except TypeError:
        print("Please enter a number.")




def test_dist_1():
    assert dist(2,4,6,8) == 5.656854249492381

def test_dist_fail_1():
    assert dist("x1", "y1", "x2", "y2") == None

def test_dist_fail_2():
    assert dist(2,4,6,8) == 5

def test_dist_2():
    assert dist(2.2,4.4,6.6,8.8) == 6.222539674441618
