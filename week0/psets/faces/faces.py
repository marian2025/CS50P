def main():
    text = input()
    after = convert(text)
    print(after)

def convert(x):
    y = x.replace(":)", "🙂")
    z = y.replace(":(", "🙁")
    return z

main()