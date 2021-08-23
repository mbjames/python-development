import random


def random_number():
    print("\n Type (r) to generate a random number. (0 - 1000)")
    print(" Type (q) to exit.")

    answer = input("\n > ")

    if answer == "r":
        x = random.randint(0, 1000)

        print("\n Number Generated:", x)

        random_number()

    elif answer == "q":
        exit()

    else:
        random_number()


random_number()
