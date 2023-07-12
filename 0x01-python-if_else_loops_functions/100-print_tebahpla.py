#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    print("{:c}{:c}".format(i, i - 32), end='')
