import math
import pytest

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

