import random


def main():
    questions = 10
    score = 0
    chances = 3
    lvl = get_level()

    while questions != 0:
        if chances == 3: # User have 3 chances to answer each equation
            # Only generate_integer for new equation if chances == 3
            x, y = generate_integer(lvl)

        try:
            user_answer = int(input(f"{x} + {y} = "))
            answer = x + y
            if user_answer == answer:
                questions -= 1
                score += 1
                chances = 3 # Reset chances to generate new equation in case user input the right answer on 2nd/3rd try
                continue
            else:
                raise ValueError
        except (ValueError):
            print("EEE")
            chances -= 1
            pass

        if chances == 0:
            print(f"{x} + {y} = {answer}")
            chances = 3 # Reset chances to generate new equation
            questions -=1
            continue

    print(f"Score: {score}")


def get_level():
    while True:
        level = input("Level: ")
        if level.isdigit() == True:
            level = int(level)
            if level > 0 and level < 4:
                return level


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


if __name__ == "__main__":
    main()