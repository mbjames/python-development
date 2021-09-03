shiny_pokemon = []


def add_pokemon():
    add_mon = input("\n Pokemon to add: ").title()
    shiny_pokemon.append(add_mon)
    print("\n " + add_mon + " has been added.")


def remove_pokemon():
    remove_mon = input("\n Pokemon to remove: ").title()
    shiny_pokemon.remove(remove_mon)
    print("\n " + remove_mon + " has been removed.")


def start():
    print("\n Welcome to your shiny list.")
    print(" To add a pokemon select (a).")
    print(" To remove a pokemon select (r).")
    print(" To view your list select (v).")
    print(" To exit select (q).")

    answer = input("\n > ").lower()

    if answer == "a":
        add_pokemon()

        start()

    elif answer == "r":
        remove_pokemon()

        start()

    elif answer == "v":
        for x in shiny_pokemon:
            print(x)

        start()

    elif answer == "q":
        exit()

    else:
        start()


start()
