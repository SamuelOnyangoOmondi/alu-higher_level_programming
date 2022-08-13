#!/usr/bin/python3
"""contains read_file function"""


def read_file(filename=""):
    """reads a text file and prints it to stdout"""
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end="")
