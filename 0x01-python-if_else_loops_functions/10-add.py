#!/usr/bin/python3
def add(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return "Invalid input"
    result = a + b

    return result
