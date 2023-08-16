#!/usr/bin/python3
"""
A Script.
"""


import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    dat = load_from_json_file("add_item.json")
except Exception:
    dat = []
arg = sys.argv
for n in range(1, len(sys.argv)):
    dat.append(arg[n])
save_to_json_file(dat, "add_item.json")
