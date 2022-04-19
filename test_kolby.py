########## Kolby Balch  kbb248 ##########

import math
import pytest



def openFile(filename):
    try:
        infile = open(filename, "r")

        print("File opened.")
    except:
        print("Invalid filename")

@pytest.mark.parametrize("values", ["testing.txt", 5, "5", False, 6.0])
def test_openFile(values):
    assert openFile(values) == None



def isPalindrome(temp):
    try:
        test = temp[::-1]

        if(test == temp):
            return True

        else:
            return False
    except:
        print("Invalid input")


@pytest.mark.parametrize("values,answer", [("testing", False), ("racecar", True), (5, None), (6.0, None), (True, None)])
def test_isPalindrome(values, answer):
    assert isPalindrome(values) == answer