import math
import pytest
from functions import *

## takes two numbers and returns
## the result of a division
def numbers(num1, num2):

    try:
        return num1 / num2
    except TypeError:
        print("Please enter a number.")

## takes in two points
## finds the distance between the points
def dist(x1, y1, x2, y2):

    try:
        dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
        dist = math.sqrt(dist)

        return dist
    except TypeError:
        print("Please enter a number.")

def openFile(filename):
    try:
        infile = open(filename, "r")

        print("File opened.")
    except:
        print("Invalid filename")


def isPalindrome(temp):
    try:
        test = temp[::-1]

        if(test == temp):
            return True

        else:
            return False
    except:
        print("Invalid input")

## returns the squareroot of a particular number
def sq(num):
    try:
        return math.sqrt(num)
    except TypeError:
        return 0
    except ValueError:
        return 0

## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    try:
        div = num1 / num2
        print("Your numbers divided is:", div)
    except ValueError:
        print("Value enter error, enter integer")
    except ZeroDivisionError:
        print("Denominator can't be equal to 0")


def test_greet():
    assert functions.greetUser("sam", "Paul", "Jordons")


## takes in a Python list
## attempts to display the item at the index provided
def displayItem(numbers, index):
    try:
        print("Your item at", index, "index is", numbers[index])
    except:
        print("an error occured")