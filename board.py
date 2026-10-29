print("Hello World!")

# 5 Factory displays for 2 players
# 7 Factory displays for 3 players
# 9 Factory displays for 4 players
factories = []
center = [0,0,0,0,0] #TODO change functions so center is nolonger factory[0]
round = 1
# 5 different tiles: Blue, Yellow, Red, Black, White

tiles = ("Blue", "Yellow", "Red", "Black", "White")

print(tiles[4])

print(f"There are {len(factories)} factories")

factories.append([0,0,0,0,0]) #need to acount for the starting tile later becuse player could chose to only grab that one, check rules
factories.append([0,2,0,1,1])
factories.append([1,0,0,2,1])
factories.append([0,1,3,0,0])
# factories.append([2,0,0,1,1])
# factories.append([1,0,0,1,2])
# factories.append([0,3,0,1,0])
# factories.append([1,0,0,0,3])
# factories.append([0,0,2,2,0])
# factories.append([0,1,2,1,0])

print(f"There are {len(factories)} factories")

def print_factories():
    for factory_index, factory in enumerate(factories):
        print(f"Factory {factory_index + 1}")
        for tile_index, tile in enumerate(factory):
            print(f"\t{tiles[tile_index]}: {tile}")

def to_center(factory):
    for tile_index, tile in enumerate(factory):
        factories[0][tile_index] += tile

def fac_draw(color, fac):
    factories[fac][color] = 0
    to_center(factories[fac])
    factories.pop(fac)
    


print("\nTesting printfactories function\n")
print(f"round {round}")
round+=1
print_factories()
fac_draw(1,1)
print(f"round {round}")
print_factories()