def safe_print_list(my_list=[], x=0):
    x_count = 0
    try:
        for y in range(x):
            print(my_list[y], end="")
            x_count += 1
    except IndexError:
        pass
    print()
    return (x_count)
