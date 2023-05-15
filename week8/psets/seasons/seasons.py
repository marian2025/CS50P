from datetime import date
import sys
import re
import inflect

p = inflect.engine()


def main():
    print(convert(input("Date of Birth: ").strip()))


def convert(s):
    if matches := re.search(r"^([1-2]\d{3})-(\d.)-(\d.)$", s):
        year = matches.group(1)
        month = matches.group(2)
        day = matches.group(3)

        try:
            d_ask = date(int(year), int(month), int(day))
            d_now = date.today()
        except:
            sys.exit("Invalid date")

        timedelta = d_now - d_ask
        days = str(timedelta).split(" ")
        # print(days[0])
        time = int(days[0]) * 24 * 60
        
        return f'{p.number_to_words(time, andword="").capitalize()} minutes'
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()