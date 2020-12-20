input = open('input.txt').read().split("\n")
blank_line = input.pop()

X = 0
Y = 1
Z = 2
W = 3


def turn_on(c, u):
    u[c] = 1
    for x in range(-1,2):
        for y in range(-1,2):
            for z in range(-1,2):
                for w in range(-1,2):
                    t = (c[X]+x, c[Y]+y, c[Z]+z, c[W]+w)
                    if (x or y or z or w) and t not in u.keys():
                        u[t] = 0


def neighbors(c, u):
    total = 0
    for x in range(-1,2):
        for y in range(-1,2):
            for z in range(-1,2):
                for w in range(-1,2):
                    t = (c[X]+x, c[Y]+y, c[Z]+z, c[W]+w)
                    if (x or y or z or w):
                        total += u.get(t, 0)
    return total


def population(u):
    total = 0
    for i in u.values():
        total += i
    return total


universe = {}

z = 0
w = 0
for y in range(len(input)):
    for x in range(len(input[y])):
        if input[y][x] == '#':
            turn_on((x, y, z, w), universe)
            
for gen in range(6):
    u = universe.copy()
    for cell in universe:
        count = neighbors(cell, universe)
        if universe[cell]:
            # If a cube is active 
            # and exactly 2 or 3 of its neighbors are also active, 
            # the cube remains active. 
            # Otherwise, the cube becomes inactive.
            if count < 2 or count > 3:
                u[cell] = 0
        else:
            # If a cube is inactive 
            # but exactly 3 of its neighbors are active, 
            # the cube becomes active. 
            # Otherwise, the cube remains inactive.
            if count == 3:
                turn_on(cell, u)
    universe = u
        
print(population(universe))
