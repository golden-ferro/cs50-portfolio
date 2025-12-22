import csv
import sys
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

arg = sys.argv[1]

if not arg.endswith(".csv"):
    sys.exit("Not a csv file")

try:
    with open(arg, "r") as file:
        reader = csv.DictReader(file)
        print(tabulate(reader, headers="keys", tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")





