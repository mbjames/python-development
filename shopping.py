shopping_list = []


def add_item():
    item = input("\n Item to add: ")
    shopping_list.append(item)
    print("\n " + item + " has been added.")


def remove_item():
    item = input("\n Item to remove: ")
    shopping_list.remove(item)
    print("\n " + item + " has been removed.")


def start():
    print("\n Welcome to your shopping list.")
    print(" Press (1) to view your list.")
    print(" Press (2) to add an item.")
    print(" Press (3) to remove an item.")

    answer = input("\n > ")

    if answer == "1":
        for x in shopping_list:
            print(x)

        start()

    elif answer == "2":
        add_item()

        start()

    elif answer == "3":
        remove_item()

        start()

    else:
        start()


start()
