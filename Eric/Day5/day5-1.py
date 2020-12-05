input = open('input.txt').read().split("\n")

# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.
# input = ['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']

# print(input)

maxid = 0
for bsp in input:
    bspa = list(bsp)
    # print(bspa)
    row = 0
    seat = 0

    if len(bspa) == 10:

        if bspa[0] == 'B':
            row += 64
        if bspa[1] == 'B':
            row += 32
        if bspa[2] == 'B':
            row += 16
        if bspa[3] == 'B':
            row += 8
        if bspa[4] == 'B':
            row += 4
        if bspa[5] == 'B':
            row += 2
        if bspa[6] == 'B':
            row += 1
        if bspa[7] == 'R':
            seat += 4
        if bspa[8] == 'R':
            seat += 2
        if bspa[9] == 'R':
            seat += 1

    seatid = row * 8 + seat
    if seatid > maxid:
        maxid = seatid
    # print(row, seat, seatid)

print(maxid)
