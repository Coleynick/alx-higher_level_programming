#!/usr/bin/python3
from typing import Dict
from print_sorted_dictionary import print_sorted_dictionary

def complex_delete(a_dictionary, value):
    keys_to_delete = [key for key, val in a_dictionary.items() if val == value]
    for key in keys_to_delete:
        a_dictionary.pop(key)
    return a_dictionary
