import csv
import sys

list = []

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if sys.argv[1].endswith(".csv") != True:
    sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(", ")
                house = row["house"]
                list.append({"first": first, "last": last, "house": house})
    except OSError:
        sys.exit(f"Could not read {sys.argv[1]}")

# print(list)

with open(sys.argv[2], 'w', newline='') as csvfile:
    fieldnames = ["first", "last", "house"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(list)
    # writer.writerow({"first": list[i]["first"], "last": list[i]["last"], "house": list[i]["house"]})

