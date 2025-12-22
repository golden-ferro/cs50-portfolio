import sys
import csv

c = 0

arg = sys.argv[1:]

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

arg = sys.argv[1]

if not arg.endswith(".py"):
    sys.exit("Not a Python file")

try:
    with open(arg, "r") as file:
        for line in file:
            line = line.lstrip() 
            if line != "" and not line.startswith("#"):
                c += 1

except FileNotFoundError:
    sys.exit("File does not exist")

print(c)
