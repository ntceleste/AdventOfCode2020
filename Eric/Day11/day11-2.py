input = open('input.txt').read().split()
area = [list(i) for i in input]

search = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1],           [0, 1],
    [1, -1],  [1, 0],  [1, 1],
]

def visible_occupied_seats(x, y):
    global search, area
    count = 0
    for xy in search:
        done = False
        xs = x
        ys = y
        while not done:
            xs += xy[0]
            ys += xy[1]
            if xs < 0 or ys < 0:
                done = True
                continue
            try:
                if area[ys][xs] == '#':
                    done = True
                    count += 1
                if area[ys][xs] == 'L':
                    done = True
            except:
                done = True
                pass
    return count


def print_area():
    global area
    for row in area:
        print(' '.join(row).replace('.', '+'))
    print()


changing = True

while changing:
    # print_area()
    changing = False
    newarea = [i[:] for i in area]
    for y in range(len(area)):
        for x in range(len(area[0])):
            seat = area[y][x]
            if seat != '.':
                count = visible_occupied_seats(x, y)
                # empty seats that see no occupied seats become occupied
                if seat == 'L' and count == 0:
                    newarea[y][x] = '#'
                    changing = True
                # it now takes five or more visible occupied seats
                # for an occupied seat to become empty 
                if seat == '#' and count >= 5:
                    newarea[y][x] = 'L'
                    changing = True
                # Otherwise, the seat's state does not change.
    area = newarea

count = 0
for row in area:
    for position in row:
        if position == '#':
            count += 1

print(count)
