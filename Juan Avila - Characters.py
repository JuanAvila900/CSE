class Character(object):
    def __init__(self, name, health, damage, description, clothes):
        self.name = name
        self.health = health
        self.damage = damage
        self.description = description
        self.stats = clothes

    def move(self):
         self.move = True
         if 'move':
             print("You Move Foward")
         else:
             print("You found a chest full of items that are useful.")
    def get(self):
        self.get = True
        if 'open':
            print("You Open the Chest")
        else:
            print("Choose an item")


Dude = Character("Cloud", "10","No Damage","He likes fighting, he hates people that think they're smarter than him"
                                           "and he loves potatoes","Battle Style chothes")

print(Dude.name)
print(Dude.health)
print(Dude.damage)
print(Dude.description)




