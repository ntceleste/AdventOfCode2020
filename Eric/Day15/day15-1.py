starting = [
    [0,3,6],
    [1,3,2], 
    [2,1,3],
    [1,2,3],
    [2,3,1],
    [3,2,1],
    [3,1,2],
    [11,18,0,20,1,7,16]
]


def previous(alist, value):
    return len(alist) - alist[-2::-1].index(value) - 1


goal = 2020

for turns in starting:
    print('starting {}'.format(turns))
    for i in range(len(turns), goal):
        last = turns[i - 1]
        try:
            prior = previous(turns, last)
            dist = len(turns) - prior
        except:
            dist = 0
        # print(dist)
        turns.append(dist)
    print(turns.pop())


