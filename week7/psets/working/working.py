import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A|P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A|P]M)$", s)
    if matches:
        match = matches.groups()
        # return match
        if (int(match[1]) > 12) or (int(match[5]) > 12):
            raise ValueError
        left_time = format(match[1], match[2], match[3])
        right_time = format(match[5], match[6], match[7])
        return left_time + " to " + right_time
    else:
        raise ValueError


def format(hour, minute, am_pm):
    if am_pm == "PM":
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)

    if minute == None:
        new_minute = ":00"
        new_time = f"{new_hour:02}" + new_minute
    else:
        new_time = f"{new_hour:02}" + ":" + minute

    return new_time


if __name__ == "__main__":
    main()