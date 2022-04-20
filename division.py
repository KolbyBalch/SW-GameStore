import math
import pytest

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
