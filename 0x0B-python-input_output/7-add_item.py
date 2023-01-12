#!/usr/bin/python3
"""
Module 7-add_item.py
"""


from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

f_name = "add_item.json"

try:
    data = load_from_json_file(f_name)
except FileNotFoundError:
    data = []

save_to_json_file(data + argv[1:], f_name)
