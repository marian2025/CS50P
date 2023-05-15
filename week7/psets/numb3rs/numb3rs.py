import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        one, two, three, four = matches.groups()
        if (-1 < int(one) < 256) and (-1 < int(two) < 256) and (-1 < int(three) < 256) and (-1 < int(four) < 256):
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()