starting = [
    [11,18,0,20,1,7,16]
]

goal = 30000000

# this method is slow (takes over 20 seconds)
# but it seems to work

for turns in starting:
    print('starting {}'.format(turns))
    seen = {}
    last_seen = 0
    for i in range(len(turns)):
        seen[turns[i]] = {
            'index': i,
            'dist': 0
        }
        last_seen = turns[i]
    for i in range(i + 1, goal):
        distance = seen[last_seen]['dist']
        dist = 0
        if distance in seen:
            dist = i - seen[distance]['index']
        seen[distance] = {
            'index': i,
            'dist': dist
        }
        last_seen = distance
        
    print(last_seen)


