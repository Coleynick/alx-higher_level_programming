#!/usr/bin/python3
for a in range(ord("z"), ord("a")-1, -1):
    if a % 2 == 1:
        y = chr(a - ord("a") + ord("A"))
    else:
        y = chr(a)
    print("{}".format(str(y)), end='')
