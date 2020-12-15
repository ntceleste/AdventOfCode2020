import crt
input = open('input.txt').read().split()
ids = [ int(e) for e in input[1].replace('x', '0').split(',') ]
# print(ids)
frequency = [ e for e in ids if e ]
# print(frequency)
# print([ ids.index(e)for e in frequency ])
rem = [ e - ids.index(e) for e in frequency ]
# print(rem)
print(crt.chinese_remainder(frequency, rem))

