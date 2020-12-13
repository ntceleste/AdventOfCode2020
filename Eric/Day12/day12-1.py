input = open('input.txt').read().split()

X = 0
Y = 1

position = [0, 0]
facing = 90 # N = 0, E = 90, S = 180, W = 270
forward = {
    0: [0, 1],
    90: [1, 0],
    180: [0, -1],
    270: [-1, 0]
}


def add_to_position(delta, factor):
    global position
    x = position[X] + delta[X] * factor
    y = position[Y] + delta[Y] * factor
    position = [x, y]


for step in input:
    action = step[0]
    distance = int(step[1:])
    move = [0, 0]
    factor = 1
    # N means to move north by the given value.
    if action == 'N':
        move = [0, distance]
    # S means to move south by the given value.
    if action == 'S':
        move = [0, 0 - distance]
    # E means to move east by the given value.
    if action == 'E':
        move = [distance, 0]
    # W means to move west by the given value.
    if action == 'W':
        move = [0 - distance, 0]
    # L means to turn left the given number of degrees.
    if action == 'L':
        facing = (facing - distance) % 360
    # R means to turn right the given number of degrees.
    if action == 'R':
        facing = (facing + distance) % 360
    # F means to move forward by the given value in the direction the ship is currently facing.
    if action == 'F':
        move = forward[facing]
        factor = distance
    add_to_position(move, factor)
    # print(action, distance, position, facing)
    
manhatten = abs(position[X]) + abs(position[Y])
print(manhatten)

