def main():
    greet = input("Greeting: ").strip().lower()
    print(f"${value(greet)}")


def value(greeting):
    if greeting.find("h",0,1) == 0 or greeting.find("H",0,1) == 0:
        if greeting.find("hello") == 0:
            return 0
        else:
            return 20
    else:
        return 100


# def value(greeting):
#     if greeting.startswith("hello"):
#         return 0
#     elif greeting.startswith("h"):
#         return 20
#     else:
#         return 100


if __name__ == "__main__":
    main()