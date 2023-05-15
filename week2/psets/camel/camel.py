def main():
    word = input("camelCase: ").strip()
    after = convert(word)
    print(f"snake_case: {after}")


def convert(text):
    for c in text:
        if c.isupper():
            text = text.replace(c, "_"+c.lower())
    return text

main()