world_map = {
    'THEDUNGEONROOM': {
        'NAME': "Dungeon",
        'DESCRIPTION': "You are inside of the Dungeon. You have nothing but different passageways that lead you into"
                       "pure darkness that will constantly lead you to death. You then find an opened treasure chest"
                       "filled with weapons like a sword, some bows and a arrow, and a shield in case you need to protect"
                       "yourself from dangers from different pathways",
        'PATHS': {
            'EAST': 'NOTHINGROOM',
        }
    },

    'NOTHINGROOM': {
        'NAME': "Empty Room",
        'DESCRIPTION':"You are in a empty room, you do nothing but see an empty pathway at the other east of the side." 
                      "You did 5 steps and a bunch of monsters approach in your way. You have two options. Fight, or" 
                      "run away like a coward.",
        'PATHS':{
            'EAST': 'EASTBATTLEFIELD',
        }
    },

    'EASTBATTLFIELD': {
        'NAME': "Battlefield Room (Room 1)",
        'DESCRIPTION':"You went into a strange looking room filled with used weapons that are broken, smeared, and"
                      "Destroyed completely, something like a...Battlefield. After you saw the whole place, you saw"
                      "another pathway that leads to another room. You procceded to go without any heisitation.",
        'PATHS':{
            'EAST': 'EASTBATTLEFIELD2',
        }
    },

    'EASTBATTLEFIELD2': {
        'NAME': 'Battlefield Room (Room 2)',
        'DESCRIPTION':"You proceeded to go foward to get to another battlefield.",
        'PATHS':{

            'SOUTH':'SECRETFILES',
        }
    },

    'SECRETFILES': {
        'NAME': 'File Room',
        'DESCRIPTION':"You went to south and found a door closed. Apparently, the door was unlocked and you opened it" 
                      "with ease. When opened, you went inside and found ten tables filled with files. you started to" 
                      "look at a file that had some secrets to this disasterous maze that tries to kill you. with that"
                      "settled, you put it in your pocket and found another way that can lead you in to pure darkness."
                      "Enter at your own risk...?",
        'PATHS': {
            'WEST': 'Genetic Room',
        }
    },

    'Genetic Room': {
        'NAME': 'Genetic Lab',
        'DESCRIPTION':"You kept going foward until you found a lab full of dangerous generic expirement bottles,"
                      "you kept looking around this awkward lab until you find some genetic creatures looking for"
                      "something to eat until it found you. You quickly got the sword and tried to defend the genetic"
                      "creature's attacks. You hit the genetic creatures with ten hits and they comepletely dissapeared."
                      "you decided that you wanted to keep looking at this place for a few seconds so you investigated"
                      "until you found a short letter of Proffesor Hugo. you put it in your pocket and found a hallway"
                      "up ahead of you. You wanted to go back, but it was locked. you were crying for help but you"
                      "had no choice but to go foward",
        'PATHS':{
            'WEST': 'Hallway'
        }
    },

    'Hallway': {
        'NAME':'Hallway',
        'DESCRIPTION':"You walked into a long hallway that leads you to another path. You started to feel a strange aura"
                      "and started to feel a bit uneased. You procceded to go with no heisitation",
        'PATHS': {
            'WEST': 'Portal'
        }
    },

    'Portal Room': {
        'NAME': 'Portal',
        'DESCRIPTION':"You kept walking until you saw the last door at the hallway.The door creaked opened, and you were"
                      "starting to get worried. you had no choice but to go inside.You slowly walked inside, there was"
                      "nothing but a portal. After you saw the portal and hastily wanted to look at it closely, the door"
                      "slammed shut and you cried for help, after few minutes of crying for help for no reason, you"
                      "looked at the portal, you realized that the portal was the only way out, but then you thought"
                      "....what if your families and your friends start to get worried? what if you start to go to"
                      "another dimension that can lead you to another world, or basically destroy everything?! You start"
                      "to get frustrated, worried, and depressed. As time passed by, you slowly walked up to the portal,"
                      "th portal was immense, and it had a beautiful ripple affect. You started to gain confidence and"
                      "went inside a portal. After a few seconds.....you never returned and the portal turned off"
                      "slowly..."
    }}


current_node = west_house
directions = ['north', 'south', 'east', 'west']
short_directions = ['n','s','e','w']

while True:
    print(current_node*********)
    print(current_node*********)
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
        elif command in short_directions
        #look for command we typed in
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            ***********

