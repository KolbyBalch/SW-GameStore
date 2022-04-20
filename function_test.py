
import math
import pytest
from functions import *

## opens a file in read mode
## filename received as a parameter
def openFile(filename):
    infile = open(filename, "r")

    print("File opened.")
@pytest.mark.parametrize("values", ["testing.txt", 5, "5", False, 6.0])
def test_openFile(values):
    assert openFile(values) == None


## takes in a string -- reverses it
## then compares the two
def isPalindrome(temp):
    test = temp[::-1]

    if(test == temp):
        return True

    else:
        return False
@pytest.mark.parametrize("values,answer", [("testing", False), ("racecar", True), (5, None), (6.0, None), (True, None)])
def test_isPalindrome(values, answer):
    assert isPalindrome(values) == answer

## takes two numbers and returns
## the result of a division
def numbers(num1, num2):
    return num1 / num2

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

    dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
    dist = math.sqrt(dist)

    return dist

def test_dist_1():
    assert dist(2,4,6,8) == 5.656854249492381

def test_dist_fail_1():
    assert dist("x1", "y1", "x2", "y2") == None

def test_dist_fail_2():
    assert dist(2,4,6,8) == 5

def test_dist_2():
    assert dist(2.2,4.4,6.6,8.8) == 6.222539674441618

## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    div = num1 / num2

    print("Your numbers divided is:", div)

def divide_inputs1():
    inputs = [8,4]
    for k in inputs:
        yield k

NUMBERS1 = divide_inputs1()

def test_divide1(monkeypatch, capfd):
    monkeypatch.setattr('builtins.input', lambda _: next(NUMBERS1))
    divide()
    out, err = capfd.readouterr()
    assert out == "Your numbers divided is: 2.0\n"

def divide_inputs2():
    inputs = [8,0]
    for k in inputs:
        yield k

NUMBERS2 = divide_inputs2()

def test_divide2(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:next(NUMBERS2))
    with pytest.raises(ZeroDivisionError):
        divide()

def divide_inputs3():
    inputs = ["txt",0]
    for k in inputs:
        yield k

NUMBERS3 = divide_inputs3()

def test_divide3(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:next(NUMBERS3))
    with pytest.raises(ValueError):
        divide()

## returns the squareroot of a particular number
def sq(num):
    return math.sqrt(num)

def test_sq1():
    assert sq(4) == 2
def test_sq2():
    assert sq(36) == 6
def test_sq3():
    assert sq(3) == math.sqrt(3)
def test_sq4():
    assert sq(2.0) == math.sqrt(2.0)
def test_sq5():
    with pytest.raises(ValueError):
        sq(-4.0)
def test_sq6():
    with pytest.raises(TypeError):
        sq("six")

## grabs user's name
## greets them by their entire name
## names should be strings
def greetUser(first, middle, last):
    print("Hello!")
    print("Welcome to the program", first, middle, last)
    print("Glad to have you!")

def test_greet():
    assert functions.greetUser("sam", "Paul", "Jordons")