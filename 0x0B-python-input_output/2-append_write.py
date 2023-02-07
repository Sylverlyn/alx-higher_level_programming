#!/usr/bin/python3
""" THis module appends a string to a txt file."""


def append_write(filename="", text=""):
    """function appends a string and returns the number of character added."""
    with open(filename, "a") as f:
        return f.write(text)
