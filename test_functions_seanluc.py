import pytest
from functions import *

def test_greet():
    assert functions.greetUser("sam", "Paul", "Jordons")