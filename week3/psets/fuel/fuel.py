def main():
    text = get_fraction("Fraction: ")
    print(text)


def get_fraction(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            procent = round(int(x)/int(y)*100)
            if 0 <= procent <= 1:
                return ("E")
            elif 99 <= procent <= 100:
                return ("F")
            elif 1 < procent < 99:
                return str(procent) + "%"
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


main()