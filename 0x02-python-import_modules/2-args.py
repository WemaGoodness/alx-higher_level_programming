#!/usr/bin/python3
import sys


def main():
    args = sys.argv
    num_args = len(args) - 1

    if num_args == 0:
        print("Number of arguments: 0.")
    elif num_args == 1:
        print(f"Number of argument: 1:")
    else:
        print(f"Number of arguments: {num_args}:")

    for i in range(1, len(args)):
        print(f"{i}: {args[i]}")


if __name__ == "__main__":
    main()
