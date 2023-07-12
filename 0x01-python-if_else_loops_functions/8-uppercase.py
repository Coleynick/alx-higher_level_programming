#!/usr/bin/python3
def uppercase(str):
    for char in str:
        print("{:c}".format(ord(char) & 223), end='')
    print()
