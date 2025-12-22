import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

read = sys.argv[1]
write = sys.argv[2]

if not read.endswith(".csv") or not write.endswith(".csv"):
    sys.exit("Not a csv file")

try:
    lines = []
    with open(read, "r") as file:
        reader = csv.reader(file)
        next(reader) #skip the first line (the header)
        for row in reader:
            names, house = row
            names = names.replace('"', '')
            first, last = names.split(", ")
            lines.append({"first": last, "last": first, "house": house})

    fieldnames = ["first", "last", "house"]
    with open(write, "w") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(lines)

except FileNotFoundError:
    sys.exit("File does not exist")

