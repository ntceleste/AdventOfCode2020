input = open('input.txt').read().split()
area = [list(i) for i in input]

search = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1],           [0, 1],
    [1, -1],  [1, 0],  [1, 1],
]

def adjacent_occupied_seats(x, y):
    global search, area
    count = 0
    for xy in search:
        xs = x + xy[0]
        ys = y + xy[1]
        if xs < 0 or ys < 0:
            continue
        try:
            if area[ys][xs] == '#':
                count += 1
        except:
            pass
    return count


def print_area():
    global area
    for row in area:
        print(''.join(row))
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
                count = adjacent_occupied_seats(x, y)
                # If a seat is empty (L) 
                # and there are no occupied seats adjacent to it, 
                # the seat becomes occupied.
                if seat == 'L' and count == 0:
                    newarea[y][x] = '#'
                    changing = True
                # If a seat is occupied (#) 
                # and four or more seats adjacent to it 
                # are also occupied, the seat becomes empty.
                if seat == '#' and count >= 4:
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
