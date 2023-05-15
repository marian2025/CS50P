def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    convert = float(d.removeprefix("$"))
    # print(f"${convert:.2f}")
    return convert


def percent_to_float(p):
    # TODO
    convert = float(p.removesuffix("%"))
    # print(f"{convert:.0f}%")
    return convert/100

main()