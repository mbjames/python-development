w = "\n We will not survive this!"

x = "\n Size does not matter!"

y = "\n I have no fear!"

z = "\n Don't pick the dwarf!"


class Player:
    def __init__(self):
        self.type = ""
        self.name = ""
        self.health = 0
        self.attack = 0
        self.defense = 0
        self.magic = ""

    def print(self):
        print("\n Type:", self.type)
        print(" Name:", self.name)
        print(" Health:", self.health)
        print(" Attack:", self.attack)
        print(" Defense:", self.defense)
        print(" Magic:", self.magic)


warrior = Player()
warrior.type = "Warrior"
warrior.name = "Hugo"
warrior.health = 100
warrior.attack = 150
warrior.defense = 50
warrior.magic = "Fire"

dwarf = Player()
dwarf.type = "Dwarf"
dwarf.name = "Roald"
dwarf.health = 100
dwarf.attack = 50
dwarf.defense = 150
dwarf.magic = "Earth"

rogue = Player()
rogue.type = "Rogue"
rogue.name = "Donovan"
rogue.health = 150
rogue.attack = 75
rogue.defense = 75
rogue.magic = "Water"

elf = Player()
elf.type = "Elf"
elf.name = "Helmer"
elf.health = 200
elf.attack = 50
elf.defense = 50
elf.magic = "Air"


def start():
    print("\n Please select a character. (1, 2, 3 or 4)")
    print(" 1. Warrior")
    print(" 2. Dwarf")
    print(" 3. Rogue")
    print(" 4. Elf")
    print("\n Press (q) to exit.")

    answer = input("\n > ")

    if answer == "q":
        exit()

    elif answer == "1":
        warrior.print()

        print(w)

        start()

    elif answer == "2":
        dwarf.print()

        print(x)

        start()

    elif answer == "3":
        rogue.print()

        print(y)

        start()

    elif answer == "4":
        elf.print()

        print(z)

        start()

    else:
        start()


start()