#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    with open(filename, 'r') as f:
        json.load(f)
