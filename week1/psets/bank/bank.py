greet = input("Greeting: ").strip().lower()

# print(greet.find("h",0,1))

if greet.find("h",0,1) == 0:
    if greet.find("hello") == 0:
        print("$0")
    else:
        print("$20")
else:
    print("$100")