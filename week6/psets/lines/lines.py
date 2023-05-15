import sys

count = 0

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if sys.argv[1].endswith(".py") != True:
    sys.exit("Not a Python file")
else:
    try:
        file = open(sys.argv[1])
    except OSError:
        sys.exit("File does not exist")

for line in file:
    if line.lstrip().startswith("#") != True and line.strip() != "":
        count += 1
        # print(line, end="")

file.close()
print(count)