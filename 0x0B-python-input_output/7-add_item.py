#!/usr/bin/python3
""" adds all arguments to a Python list, and then save them to a file"""


import sys
import json
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"

if os.path.isfile(file):
    my_list = load_from_json_file(file)

else:
    my_list = []

for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])
save_to_json_file(my_list, file)
