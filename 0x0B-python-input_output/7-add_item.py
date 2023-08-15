#!/usr/bin/python3
"""
A Script.
"""


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    dat = load_from_json_file("add_item.json")
except Exception:
    dat = []

for n in sys.argv[1:]:
    dat.append(n)
save_to_json_file(dat, "add_item.json")
