input = open('input.txt').read().split("\n")
input.pop() # remove blank line

mask0 = 0
mask1 = 0
mem = {}

for line in input:
    parts = line.split(' = ')
    # print(parts)
    if parts[0] == 'mask':
        mask1 = int(parts[1].replace('X', '0'), 2)
        mask0 = int(parts[1].replace('1', 'X').replace('0', '1').replace('X', '0'), 2)
        # print('mask0 = {0:010b}\nmask1 = {1:010b}'.format(mask0, mask1))
    else:
        key = int(parts[0][4:-1])
        value = int(parts[1])
        mem[key] = abs(~(~value | mask0)) | mask1
# masked = abs(~(~value | mask0)) | mask1

# print(mem)
print(sum([value for key, value in mem.items()]))
