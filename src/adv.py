from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons",
                    ["sword", "coins"]),

    'foyer':    Room("Foyer",
                    """Dim light filters in from the south. Dusty passages run north and east.""",
                    ["armor", "coins"]),

    'overlook': Room("Grand Overlook",
                    """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
                    ["water", "coins"]),

    'narrow':   Room("Narrow Passage",
                    """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
                    ["food", "coins"]),

    'treasure': Room("Treasure Chamber",
                    """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""",
                    ["stick", "coins"]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].e_to = None
room['outside'].s_to = None
room['outside'].w_to = None
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = None
room['overlook'].n_to = None
room['overlook'].e_to = None
room['overlook'].s_to = room['foyer']
room['overlook'].w_to = None
room['narrow'].n_to = room['treasure']
room['narrow'].e_to = None
room['narrow'].s_to = None
room['narrow'].w_to = room['foyer']
room['treasure'].n_to = None
room['treasure'].e_to = None
room['treasure'].s_to = room['narrow']
room['treasure'].w_to = None

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
directions = ['n', 'e', 's', 'w']

while True:
    current_room = player.get_current_room()
    north = current_room.n_to
    east = current_room.e_to
    south = current_room.s_to
    west = current_room.w_to

    print(f'\n{player}')
    print('\nDirecions Available:\n',f'North: {north.name}\n' if north else '', f'East: {east.name}\n' if east else '', f'South: {south.name}\n' if south else '', f'West: {west.name}\n' if west else '')
    direction = input("-> ")
    if direction in directions:
        if direction == 'n':
            if north:
                player.set_current_room(north)
            else:
                print('Can\'t go North')
        elif direction == 'e':
            if east:
                player.set_current_room(east)
            else:
                print('Can\'t go East')
        elif direction == 's':
            if south:
                player.set_current_room(south)
            else:
                print('Can\'t go South')
        elif direction == 'w':
            if west:
                player.set_current_room(west)
            else:
                print('Can\'t go West')
    elif 'take' in direction or 'get' in direction:
        item = direction.split()[1]
        if item in current_room.get_items():
            current_room.remove_item(item)
            player.add_item(item)
        else:
            print('You couldn\'t seem to find that item!')
    elif 'drop' in direction:
        item = direction.split()[1]
        if item in player.get_items():
            player.remove_item(item)
            current_room.add_item(item)
        else:
            print('You couldn\'t seem to find that item!')
    elif direction == 'q':
        print("Exiting Program...")
        break
    else:
        print('Invalid Input.')