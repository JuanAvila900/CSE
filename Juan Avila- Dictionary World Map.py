world_map = {
    'WESTHOUSE': {
        'NAME': "West of House",
        'DESCRIPTION': "You are west of a white house",
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'SOUTH':'SOUTHHOUSE'
        }
    },}

current_node = world_map['WESTHOUSE']
directions = ['NORTH']

while True:
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions :
      try:
          Name_of_code = current_node['PATHS'][command]
          current_node = world_map[Name_of_code]
      except KeyError:
          print("You cannot go go this way")
    else:
        print('Command not recognized')
