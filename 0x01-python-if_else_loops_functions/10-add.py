#!/usr/bin/python3
def add(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both values must be integers")
    result = a + b

    return result
