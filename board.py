factories = []
center = [0,0,0,0,0]
round = 1
num_players = 0

# 5 different tiles: Blue, Yellow, Red, Black, White
tiles = ("Blue", "Yellow", "Red", "Black", "White")
BLUE = 0
YELLOW = 1
RED = 2
BLACK = 3
WHITE = 4

# 5 Factory displays for 2 players
# 7 Factory displays for 3 players
# 9 Factory displays for 4 players
factories.append([0,1,2,1,0]) #need to acount for the starting tile later becuse player could chose to only grab that one, check rules
factories.append([0,2,0,1,1])
factories.append([1,0,0,2,1])
factories.append([0,1,3,0,0])
# factories.append([2,0,0,1,1])
# factories.append([1,0,0,1,2])
# factories.append([0,3,0,1,0])
# factories.append([1,0,0,0,3])
# factories.append([0,0,2,2,0])

def print_factories(): # Prints the contents of each factory
    for factory_index, factory in enumerate(factories):
        print(f"Factory {factory_index + 1}")
        for tile_index, tile in enumerate(factory):
            print(f"\t{tiles[tile_index]}: {tile}")

def to_center(factory): # Moves the contents of a factory to the center
    for tile_index, tile in enumerate(factory):
        center[tile_index] += tile

def fac_draw(color, fac): # Takes a factory and tile color and executes a turn
    if factories[fac][color] == 0:
        raise ValueError("The factory does not contain the tile being drawn")
    factories[fac][color] = 0
    to_center(factories[fac])
    factories.pop(fac)

def factories_with(color): # Returns the number of factories with a specific tile
    num_with_color = 0

    for factory in factories: # Checks turns in factories
        if factory[color] > 0:
            num_with_color += 1

    return num_with_color

def turns_left():
    turns = 0
    for i in center:
        if i > 0:
            turns += 1
    return turns

def max_turns(): # Maximum turns comes from clearing out the center before drawing from a factory
    turns = 0
    
    for i in center: # Checks turns in center
        if i > 0:
            turns += 1
    
    for factory in factories: # Checks turns in factories
        for i in factory:
            if i > 0:
                turns += 1
    
    return turns

def min_turns(): # Minimum turns comes from clearing out the factories before drawing from the center. Tiles pushed to the center should already be represented in the center when possible
    turns = 0
    
    for i in center: # Checks turns in center
        if i > 0:
            turns += 1

    #TODO could be generalized. The strategy of adding the turns in center to the number of factories works whenever all the tiles in a factory are already reprecented in the center
    if turns == 5: # The case when the center already has all the diferent types of tiles. Min turn
        turns += len(factories)
    
    # Does the order the factories are drawn from matter? No the center will always be pulled last
    # Can every turn number between min and max be achived?

    return turns

print("\nTesting printfactories function\n")
print(f"round {round}")
round+=1
print(center)
print_factories()

print(f"round {round}")
round+=1
fac_draw(YELLOW,1)
print(center)
print_factories()
print(f"At most {max_turns()} more turns could be taken")

print(f"round {round}")
round+=1
fac_draw(BLACK,1)
print(center)
print_factories()
print(f"There are {turns_left()} turns remaining in the center")
print(f"At most {max_turns()} turns remain")
print(f"There will be at least {min_turns()} more turns")