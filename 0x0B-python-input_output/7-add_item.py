#!/usr/bin/python3


"""Saving arguments to a list"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    lst = load_from_json_file("add_item.json")
except:
    lst = []

for val in sys.argv[1:]:
    lst.append(val)
save_to_json_file(lst, "add_item.json")
