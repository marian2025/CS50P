from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
fonts = figlet.getFonts()
rand = random.choice(fonts)

if len(sys.argv) == 1:
    text = input("Input: ")
    print("Output: ", Figlet(font=rand).renderText(text), sep="\n")
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "-font":
        if sys.argv[2] in fonts:
            text = input("Input: ")
            print("Output: ", Figlet(font=sys.argv[2]).renderText(text), sep="\n")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")