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


THEDUNGEONROOM = Room("Dungeon", "You are inside of the Dungeon. You have nothing but different passageways"
                                 "that'll lead you into"
                                 "pure darkness that will constantly lead you to"
                                 "death.You then find an opened treasure chest"
                                 "filled with weapons like a sword, some bows and a arrow, and a"
                                 "shield in case you need to prlotect."
                                 "Pick a weapon in order to proceed."
                                 "yourself from dangers from different pathways", None, None, 'NOTHINGROOM', None)
NOTHINGROOM = Room("Empty Room", "You are in a empty room, you do nothing but see an empty"
                                 "pathway at the other east of the side." 
                                 "You did 5 steps and a bunch of monsters approach in your way.",
                                 None, None, 'BattleField_Room_(Room 1)', None)
EASTBATTLEFIELD = Room("BattleField Room (Room 1)", "You went into a strange looking room filled with used weapons"
                                                    "that are broken, smeared, and"
                                                    "Destroyed completely, something like a...Battlefield. "
                                                    "After you saw the whole place, you saw"
                                                    "another pathway that leads to another room. You proceeded to "
                                                    "go.", None, None,
                                                    'Battle field room (Room 2)', None)
EASTBATTLEFIELD2 = Room("BattleField Room (Room 2)", "You proceeded to go forward to get to another battlefield.", None,
                        None, None, 'File room')
SECRETFILES = Room("File Room", "You went to south and found a door closed. Apparently, the door was unlocked and you "
                                "opened it" 
                                "with ease. When opened, you went inside and found ten"
                                "tables filled with files. you started to" 
                                "look at a file that had some secrets to this"
                                "disastrous maze that tries to kill you. with that"
                                "settled, you put it in your pocket and found another"
                                "way that can lead you in to pure darkness."
                                "Enter at your own risk...?", None, None, None, 'Genetic Room')
GeneticRoom = Room("Genetic Lab", "You kept going forward until you found a lab full of dangerous generic experiment"
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
                          "and started to feel a bit....down. You proceeded to go with no worry",
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
                            "the portal was immense, and it had a beautiful ripple affect. "
                            "You started to gain confidence and"
                            "went inside a portal. After a few seconds.....you never returned and the portal turned off"
                            "slowly", 'SECRET', None, None, None)
SECRET = Room("Mystery Room", "You failed. You were in a dark void full of nothingness. You started to yell all "
                              "around you, but no sign of hope."
                              "You could'nt do nothing but curl yourself in a ball and "
                              "mummer something...for a split second,"
                              " you see"
                              "nothing and started to fall asleep. Then you started to think that "
                              "the portal wasn't a portal."
                              "...."
                              "....it was a TRAP.", 'TheTrapRoom', None, None, None)
TheTrapRoom = Room("TheTrapRoom", "Few hours later, you woke up from Sleeping gas that caused you to sleep while you"
                   "thought that you were dying." 
                   "You looked around and see an iron door. You ran to the iron door, and tried to open, but it was"
                   "locked. you needed to find the right key that can" 
                   "Fit the keyhole.", 'Unknown General Base', None, None, None)
UnknownGeneralbase = Room("Old Base", "Once you found an iron key, you opened the iron door with ease,"
                                      " and went outside."
                          "You found out that you were in an old base that was probably destroyed ten years"
                          "ago. You started to look around and found some better weapons, like a Dual"
                          "Wielding Sword, A Power gauntlet, A Diamond sword, And...An Egg and "
                          "Pizza for hunger, and a reinforced iron shield. you have two options.",
                          'DefencesRoom', None, None, None)
DefensivesRoom = Room("The Defensive room", "You kept walking and walking until you saw a room full of defences. you"
                                            "Went inside and some some people who're from an abandoned organization"
                                            "that went completely dead since the 19th century. Instead, you chose to"
                                            "fight. If you win, then you can proceed to the next stage.", None, None,
                                            'The Jewels Room', 'Hallway')
Jewels = Room("TheJewelsRoom", "You saw an exit that can lead you outside, you ran but you saw a room full of jewels."
                               "you went to the room and stealed ten jewels. You put the jewels in your backpack"
                               "and decided to go back.", None, None, None, 'DefencesRoom')
DefensivesRoom2 = Room("The Defensive room (again)", "You came back from the room"
                       "and saw the hallway.", None, None, None, 'Hallway')

Hallway2 = Room("The Hallway (again)", "You walked straight so you can leave this place that smelled like dead fish.",
                'Outside', None, None, None)

Outside = Room("The Outside", "You finally left the dungeon. Your quest is now over", None, None, None, None)

current_node = THEDUNGEONROOM
directions = ['north', 'west', 'east', 'south']
short_directions = ['n', 'w', 'e', 's']

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_') .lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")
