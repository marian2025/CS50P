import csv
import sys
from tabulate import tabulate

list = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if sys.argv[1].endswith(".csv") != True:
    sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                list.append(row)
    except OSError:
        sys.exit("File does not exist")

file.close()
print(tabulate(list, headers="keys", tablefmt="grid"))