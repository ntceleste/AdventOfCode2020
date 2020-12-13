input = open('input.txt').read().split()

X = 0
Y = 1

position = [0, 0]
waypoint = [10, 1]


def add_to_position(delta, factor):
    global position
    x = position[X] + delta[X] * factor
    y = position[Y] + delta[Y] * factor
    position = [x, y]


def add_to_waypoint(delta, factor):
    global waypoint
    x = waypoint[X] + delta[X] * factor
    y = waypoint[Y] + delta[Y] * factor
    waypoint = [x, y]


def move_toward_waypoint(factor):
    global waypoint
    add_to_position(waypoint, factor)
    


for step in input:
    action = step[0]
    distance = int(step[1:])
    move = [0, 0]
    factor = 1
    # N means to move the waypoint north by the given value
    if action == 'N':
        move = [0, distance]
    # S means to move the waypoint south by the given value.
    if action == 'S':
        move = [0, 0 - distance]
    # E means to move the waypoint east by the given value.
    if action == 'E':
        move = [distance, 0]
    # W means to move the waypoint west by the given value.
    if action == 'W':
        move = [0 - distance, 0]
    # L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
    if action == 'L':
        for i in range(int(distance / 90)):
            waypoint = [0 - waypoint[Y], waypoint[X]]
    # R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
    if action == 'R':
        for i in range(int(distance / 90)):
            waypoint = [waypoint[Y], 0 - waypoint[X]]
    # F means to move forward to the waypoint a number of times equal to the given value.
    if action == 'F':
        add_to_position(waypoint, distance)
        
    add_to_waypoint(move, factor)
    print(action, distance, position, waypoint)
    
manhatten = abs(position[X]) + abs(position[Y])
print(manhatten)

