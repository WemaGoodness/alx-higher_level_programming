#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5
    print("{:d} + {:d} = {}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {}".format(a, b, div(a, b)))


if __name__ == "__main__":
    main()