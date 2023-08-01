#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    x_count = 0
    try:
        for y in range(x):
            if isinstance(my_list[y], int):
                print("{:d}".format(my_list[y]), end="")
                x_count += 1
    except (IndexError, ValueError, TypeError):
        pass
    print("")
    return (x_count)
