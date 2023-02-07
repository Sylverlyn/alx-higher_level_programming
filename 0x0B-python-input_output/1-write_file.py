#!/usr/bin/python3
""" This module writes a string to a text file."""


def write_file(filename="", text=""):
    """ Function returns the the number of characters written."""
    with open(filename, "w", encoding="utf-8")as f:
        return f.write(text)
