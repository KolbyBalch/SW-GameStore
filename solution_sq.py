import math

def sqNum(num):
    try:
        return math.sqrt(num)
    except TypeError:
        return 0
    except ValueError:
        return 0