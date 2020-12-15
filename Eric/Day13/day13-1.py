input = open('input.txt').read().split()
ts = int(input[0])
ids = [ int(e) for e in input[1].replace('x', '0').split(',') ]

print(ts, ids)

earliest = {
    'id': 0,
    'wait': 9999999
}
for id in ids:
    if not id:
        continue
    wait = id - ts % id
    if wait < earliest['wait']:
        earliest['id'] = id
        earliest['wait'] = wait

print(earliest['id'] * earliest['wait'])
