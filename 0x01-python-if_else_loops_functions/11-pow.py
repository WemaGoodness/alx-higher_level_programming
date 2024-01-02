#!/usr/bin/python3
def pow(a, b):
    if not (isinstance(a, int) or isinstance(a, float) or not isinstance(b, int)
    or isinstance(b, float)):
        raise ValueError("Both values must be integers")
    result = a ** b

    return result
