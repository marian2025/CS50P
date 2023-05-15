def main():
    before = input("Input: ").strip()
    after = convert(before)
    print(f"Output: {after}")


def convert(text):
    vowels = ["a", "e", "i", "o", "u"]

    for c in text:
        if c.lower() in vowels:
            text = text.replace(c, "")
    return text


main()