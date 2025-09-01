#!/usr/bin/python3
import sys

# If no arguments besides script name, show usage
if len(sys.argv) < 2:
    print("Usage: ./args_printer.py <arg1> <arg2> ...")
    sys.exit(1)

# Enumerate to show index and value
for index, arg in enumerate(sys.argv):
    print(f"Argument {index}: {arg}")
