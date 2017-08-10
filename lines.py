#!/usr/bin/env python

from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        print "Usage: python lines.py <FILENAME>"
        exit(1)
    input_filename = argv[1]
    n_lines = 0
    try:
        with open(input_filename, "r") as file_var:
            for ln in file_var:
                n_lines += 1
    except IOError:
        print "Error: such file doesn't exist."
    print n_lines
    exit(0)
