#!/usr/bin/python3
"""
7. Load, add, save
"""
import sys

FILE = "add_item.json"

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

obj_str = list()
try:
    obj_str.extend(load_from_json_file(FILE))
except FileNotFoundError:
    pass

if len(sys.argv) > 1:
    obj_str.extend(sys.argv[1:])
save_to_json_file(obj_str, FILE)
