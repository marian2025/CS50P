def main():
    text = input("What time is it? ").strip()
    clock = convert(text)

    if 7.0 <= clock <= 8.0:
        print("breakfast time")
    elif 12.0 <= clock <= 13.0:
        print("lunch time")
    elif 18.0 <= clock <= 19.0:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")

    hours = float(hours)
    minutes = float(minutes)/60

    return hours + minutes


if __name__ == "__main__":
    main()