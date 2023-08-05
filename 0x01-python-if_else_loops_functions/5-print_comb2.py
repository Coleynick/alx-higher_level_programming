#!/usr/bin/python3
for a in range(100):
    if a > 98:
        print("{}".format(a))
    else:
        print("{:02d}, ".format(a), end='')
