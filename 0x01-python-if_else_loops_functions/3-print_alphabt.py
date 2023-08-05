#!/usr/bin/python3
for ascii_val in range(ord('a'), ord('z') + 1):
    if ascii_val == ord('q') or ascii_val == ord('e'):
        continue
    print("{}".format(chr(ascii_val)), end='')
