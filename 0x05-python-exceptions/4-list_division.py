#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    total = []
    for y in range(list_length):
        try:
            a = float(my_list_1[y]) if y < len(my_list_1) else 0.0
            b = float(my_list_2[y]) if y < len(my_list_2) else 1.0
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
        finally:
            pass
    return (total)
