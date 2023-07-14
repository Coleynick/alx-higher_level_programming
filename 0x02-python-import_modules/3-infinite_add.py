#!/usr/bin/python3
import sys

def main():
    if len(sys.argv) == 1:
        print(0)
    else:
        result = sum(int(arg) for arg in sys.argv[1:])
        print(result)


if __name__ == "__main__":
    main()
