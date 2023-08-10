#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if ord(a) >= ord("a") and ord(a) <= ord("z"):
            cap = chr(ord(a) - ord("a") + ord("A"))
        else:
            cap = a
        print("{}".format(cap), end='')
    print()
