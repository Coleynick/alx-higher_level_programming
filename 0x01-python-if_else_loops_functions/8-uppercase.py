#!/usr/bin/python3
def uppercase(str):
    for char in str:
        print("{:c}".format(char.upper()), end='')
    print()
