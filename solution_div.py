import math
def divideNum():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    try:
        div = num1 / num2
        print("Your numbers divided is:", div)
    except ValueError:
        print("Value enter error, enter integer")
    except ZeroDivisionError:
        print("Denominator can't be equal to 0")