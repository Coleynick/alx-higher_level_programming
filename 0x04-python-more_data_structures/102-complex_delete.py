#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_delete = [key for key, val in a_dictionary.items() if val == value]
    for key in keys_to_delete:
        a_dictionary.pop(key)
    return a_dictionary

def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
