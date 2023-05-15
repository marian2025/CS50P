text = input("Expression: ").strip().lower()

words = text.split()

x = float(words[0])
y = words[1]
z = float(words[2])

match y:
    case "+":
        sum = x + z
        print(f"{sum:.1f}")
    case "-":
        sum = x - z
        print(f"{sum:.1f}")
    case "*":
        sum = x * z
        print(f"{sum:.1f}")
    case "/":
        sum = x / z
        print(f"{sum:.1f}")
