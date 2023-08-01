#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    total = []
    for y in range(list_length):
        try:
            a = my_list_1[y]
            b = my_list_2[y]
            total_division = a / b
            total.append(total_division)
        except ZeroDivisionError:
            print("division by 0")
            total.append(0)
        except (ValueError, TypeError):
            print("wrong type")
            total.append(0)
        except IndexError:
            print("out of range")
            total.append(0)
        finally:
            pass
    return (total)
