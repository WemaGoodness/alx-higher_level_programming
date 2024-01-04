#!/usr/bin/python3
import hidden_4


def main():
    names = dir(hidden_4)
    filtered_names = [name for name in names if not name.startswith('__')]
    for name in sorted(filtered_names):
        print("{}".format(name))


if __name__ == "__main__":
    main()
