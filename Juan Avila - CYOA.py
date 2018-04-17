class Item(object):
    def __init__(self, name):
        self.name = name

    def name(self):
        print("You got a %s" % self.name)


class Weapon(Item):
    def __init__(self, name, weight, skill, description):
        super(Weapon, self).__init__(name)
        self.weight = weight
        self.skill = skill
        self.description = description

    def weight(self):
        print("It weighs in at 50.5")

    def ability(self):
        print("Ability 'Rage' activated")

    def description(self):
        print("You Got a %s!  Now you can start fighting off monsters!!" % self.name)


class Sword(Weapon):
    def __init__(self, name, skill, weight, description):
        super(Sword, self).__init__('Sword', description, skill, weight)


class Bow(Weapon):
    def __init__(self, name, skill, weight, description):
        super(Bow, self).__init__('Bow', skill, weight, description)


class SilverSword(Weapon):
    def __init__(self, name, skill, weight, description):
        super(SilverSword, self).__init__('Silver Sword', description, skill, weight)


class HpSword(Weapon):
    def __init__(self, name, skill, weight, description):
        super(HpSword, self).__init__(' Hp Sword', description, skill, weight)


class Xbow(Weapon):
    def __init__(self, name, skill, weight, description):
        super(Xbow, self).__init__('Xbow', description, skill, weight)


class Bombs(Weapon):
    def __init__(self, name, skill, weight, description):
        super(Bombs, self).__init__('Bombs', description, skill, weight)


class CrystalSword(Weapon):
    def __init__(self, name, skill, weight, description):
        super(CrystalSword, self).__init__('CrystalSword', description, skill, weight)


class ManaSword(Weapon):
    def __init__(self, name, skill, weight, description):
        super(ManaSword, self).__init__('ManaSword', description, skill, weight)


class consumable(Item):
    def __init__(self, name, description, effect):
        super(consumable, self).__init__(name)
        self.description = description
        self.effect = effect

    def description(self):
        print("This is a %s. Use it wisely. Lel." % self.name)

    def effect(self):
        print("This %s that you got has an effect!" % self.name)


class Potion(consumable):
    def __init__(self, name, description, effect):
        super(Potion, self).__init__('Potion', description, effect)


class HealthPotion(Potion):
    def __init__(self, name, description, effect):
        super(HealthPotion, self).__init__('Health Potion', description, effect)


class ManaPotion(Potion):
    def __init__(self, name, weight, description, effect):
        super(ManaPotion, self).__init__('ManaPotion', description, effect)


class RevivePotion(Potion):
    def __init__(self, name, weight, description, effect):
        super(RevivePotion, self).__init__('Revive Potion', description, effect)


class PoisonPotion(Potion):
    def __init__(self, name, description, effect):
        super(PoisonPotion, self).__init__('Poison Potion', description, effect)


class Food(consumable):
    def __init__(self, name, description, effect):
        super(Food, self).__init__('Food', description, effect)


class soup(Food):
    def __init__(self, name, description, effect):
        super(soup, self).__init__('soup', description, effect)


class oldhamburger(Food):
    def __init__(self, name, description, effect):
        super(oldhamburger, self).__init__('Old hamburger', description, effect)


class Orangechicken(Food):
    def __init__(self, name, description, effect):
        super(Orangechicken, self).__init__('Orange Chicken', description, effect)


class Clothing(consumable):
    def __init__(self, name, description, effect):
        super(Clothing, self).__init__(name, description, effect)


class Nikeshoes(Clothing):
    def __init__(self, name, description, effect):
        super(Nikeshoes, self).__init__('Nikeshoes', description, effect)


class LevisPants(Clothing):
    def __init__(self, name, description, effect):
        super(LevisPants, self).__init__('Levis Pants', description, effect)


class HolisterShirt(Clothing):
    def __init__(self, name, description, effect):
        super(HolisterShirt, self).__init__('Holister shirt', description, effect)

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
             print("You Move Forward")
         else:
             print("You found a chest full of items that are useful.")
    def get(self):

        self.get = True
        if 'open':
            print("You Open the Chest")
        else:
            print("Choose an item")


Dude = Character("Cloud", "10", "No Damage", "He likes fighting, he hates people that think they're smarter than him"
                                           "and he loves potatoes", "Battle Style Clothes")

print(Dude.name)
print(Dude.health)
print(Dude.damage)
print(Dude.description)


class Room(object):
    def __init__(self, name, description, north, west, east, south):
        self.name = name
        self.description = description
        self.north = north
        self.west = west
        self.east = east
        self.south = south

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


THEDUNGEONROOM = Room("Dungeon", "You are inside of the Dungeon.You have nothing but different passageways"
                                 "that'll lead you into"
                                 "pure darkness that will constantly lead you to"
                                 "death.You then find an opened treasure chest"
                                 "filled with weapons like a sword, some bows and a arrow, and a"
                                 "shield in case you need to protect."
                                 "Pick a weapon in order to proceed."
                                 "yourself from dangers from different pathways", None, None, 'NOTHINGROOM', None)

NOTHINGROOM = Room("Empty Room", "You are in a empty room, you do nothing but see an empty"
                                 "pathway at the other east of the side." 
                                 "You did 5 steps and a bunch of monsters approach in your way.",
                                 None, None, 'EASTBATTLEFIELD', None)

EASTBATTLEFIELD = Room("BattleField Room (Room 1)", "You went into a strange looking room filled with used weapons"
                                                    "that are broken, smeared, and"
                                                    "Destroyed completely, something like a...Battlefield. "
                                                    "After you saw the whole place, you saw"
                                                    "another pathway that leads to another room. You proceeded to "
                                                    "go without any hesitation.", None, None,
                       'Battle field room (Room 2)', None)

EASTBATTLEFIELD2 = Room("BattleField Room (Room 2)", "You proceeded to go forward to get to another battlefield.", None,
                        None, None, 'SECRETFILES')

SECRETFILES = Room("File Room", "You went to south and found a door closed. Apparently, the door was unlocked and you "
                                "opened it" 
                                "with ease. When opened, you went inside and found ten"
                                "tables filled with files. you started to" 
                                "look at a file that had some secrets to this"
                                "disastrous maze that tries to kill you. with that"
                                "settled, you put it in your pocket and found another"
                                "way that can lead you in to pure darkness."
                                "Enter at your own risk...?", None, None, None, 'Genetic Room')

GeneticRoom = Room("Genetic Lab", "You kept going forward until you found a lab full of dangerous generic expirement"
                                  " bottles,"
                                  "you kept looking around this awkward lab until you"
                                  "find some genetic creatures looking for"
                                  "something to eat until it found you. You quickly got the sword and"
                                  "tried to defend the genetic"
                                  "creature's attacks. You hit the genetic creatures with ten"
                                  "hits and they completely disappeared."
                                  "you decided that you wanted to keep looking at this place"
                                  "for a few seconds so you investigated"
                                  "until you found a short letter of Professor Hugo. you put it in your"
                                  "pocket and found a hallway"
                                  "up ahead of you. You wanted to go back, but it was locked."
                                  "you were crying for help but you"
                                  "had no choice but to go forward", None, 'Hallway', None, None)

Hallway = Room("Hallway", "You walked into a long hallway that leads you to another path. You started to feel"
                          "a strange aura"
                          "and started to feel a bit unease. You proceeded to go with no hesitation",
                          None, 'Portal', None, None)

PortalRoom = Room("Portal", "You kept walking until you saw the last door at the hallway.The door creaked opened,"
                            "and you were"
                            "starting to get worried. you had no choice but to go inside."
                            "You slowly walked inside, there was"
                            "nothing but a portal. After you saw the portal and hastily wanted"
                            "to look at it closely, the door"
                            "slammed shut and you cried for help, after few minutes of crying for"
                            "help for no reason, you"
                            "looked at the portal, you realized that the portal was the only way"
                            "out, but then you thought"
                            "....what if your families and your friends start to get worried?"
                            "what if you start to go to"
                            "another dimension that can lead you to another world, or"
                            "basically destroy everything?! You start"
                            "to get frustrated, worried, and depressed. As time passed by,"
                            " you slowly walked up to the portal,"
                            "the portal was immense, and it had a beautiful ripple affect."
                            "You started to gain confidence and"
                            "went inside a portal. After a few seconds.....you never returned and the portal turned off"
                            "slowly", 'SECRET', None, None, None)

SECRET = Room("Mystery Room", "You failed. You were in a dark void full of nothiness. You started to yell all "
                              "around you, but no sign of hope."
                              "You could'nt do nothing but curl yourself in a ball and "
                              "mummer something...for a split second,"
                              " you see"
                              "nothing and started to fall asleep. Then you started to think that "
                              "the portal wasn't a portal."
                              "...."
                              "....it was a TRAP.", 'TheTrapRoom', None, None, None)

TheTrapRoom = Room("TheTrapRoom", "Few hours later, you woke up from Sleeping gas that caused you to sleep while you "
                   "thought that you were dying." 
                   "You looked around and see an iron door. You ran to the iron door, and tried to open, but it was"
                   "locked. you needed to find the right key that can" 
                   "Fit the keyhole.", 'Unknown General Base', None, None, None)

UnknownGeneralbase = Room("Old Base", "Once you found an iron key, you opened the iron door with ease,"
                          "and went outside."
                          "You found out that you were in an old base that was probably destroyed ten years"
                          "ago. You started to look around and found some better weapons, like a Dual"
                          "Wielding Sword, A Power gauntlet, A Diamond sword, And...An Egg and "
                          "Pizza for hunger, and a reinforced iron shield. you have two options.",
                          'DefencesRoom', None, None, None)

DefencesRoom = Room("The Defensive room", "You kept walking and walking until you saw a room full of defences. you"
                                          "Went inside and some some people who're from an abandoned organization"
                                          "that went completely dead since the 19th century. Instead, you chose to"
                                          "fight. If you win, then you can proceed to the next stage.", None, None,
                                          'The Jewels Room', 'Hallway')

Jewels = Room("TheJewelsRoom", "You saw an exit that can lead you outside, you ran but you saw a room full of jewels."
                               "you went to the room and stole ten jewels. You put the jewels in your backpack"
                               "and decided to go back.", None, None, None, 'DefencesRoom')

DefencesRoom2 = Room("The Defensives room (again)", "You came back from the room"
                                                    "and saw the hallway.", None, None, None, 'Hallway')


Hallway2 = Room("The Hallway (again)", "You walked straight so you can leave this place that smelled like dead fish.",
                'Outside', None, None, None)


Outside = Room("The Outside", "While you were walking, you saw a bright light out of the base room. you proceeded"
                              "to walk at the moment until you found the last monster blocking the path. you decided to"
                              "fight because you want to end it right now", None, None, None, None)
