class Enemy:
    def __init__(self):
        self.name = ''
        self.attack = 0
        self.defense = 0
        self.health = 0
        self.magic = ''
        self.abilities = ''

bear = Enemy()
bear.name = 'Bear'
bear.attack = 100
bear.defense = 50
bear.health = 50
bear.magic = 'Earth'
bear.abilities = 'Double Strike'

print(bear.name)
print(bear.attack)
print(bear.defense)
print(bear.health)
print(bear.magic)
print(bear.abilities)
