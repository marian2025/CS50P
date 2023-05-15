import random

while True:
    level = input("Level: ")
    if level.isdigit() == True:
        if int(level) > 0:
            # print(level)
            break

number = random.randint(1, int(level))

# print(number)

while True:
    guess = input("Guess: ")
    if guess.isdigit() == True:
        if int(guess) > 0:
            if int(guess) > number:
                print("Too large!")
            elif int(guess) < number:
                print("Too small!")
            else:
                print("Just right!")
                break