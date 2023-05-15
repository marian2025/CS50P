from PIL import Image, ImageOps
from os import path
import sys


list = [".jpg", ".jpeg", ".png"]

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    if path.splitext(sys.argv[1])[1] not in list:
        sys.exit("Invalid input")
    elif path.splitext(sys.argv[2])[1] not in list:
        sys.exit("Invalid output")
    else:
        if path.splitext(sys.argv[1])[1] != path.splitext(sys.argv[2])[1]:
            sys.exit("Input and output have different extensions")

# print(path.splitext(sys.argv[1])[1])

before = Image.open(sys.argv[1])
before_size = before.size

template = Image.open("shirt.png")
template_size = template.size

# print(before.format, before.size, before.mode)
# print(template_size)

after = ImageOps.fit(before, template_size)

after.paste(template, template)
after.save(sys.argv[2])
