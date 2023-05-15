import inflect

p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
        break

mylist = p.join(names)
print("Adieu, adieu, to", mylist)


# # JOIN WORDS INTO A LIST:

# mylist = p.join(("apple", "banana", "carrot"))
# # "apple, banana, and carrot"

# mylist = p.join(("apple", "banana"))
# # "apple and banana"

# mylist = p.join(("apple", "banana", "carrot"), final_sep="")
# # "apple, banana and carrot"