#!/usr/bin/python3
def magic_calculation(a, b):
    total = 0

    for y in range(1, 3):
        try:
            if y > a:
                raise Exception('Too far')
            total += (a ** b) / y
        except Exception:
            total = b + a
            break
    return (total)
