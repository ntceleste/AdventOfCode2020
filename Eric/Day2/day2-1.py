input = open('input.txt').read().split("\n")

def parts(x):
	l = x.split()
	if len(l) == 3:
		l[0] = list(map(int,l[0].split('-')))
		l[1] = l[1].replace(':', '')
	return l

entries = list(map(parts, input))

valid = 0
for entry in entries:
	if len(entry) != 3:
		continue
	c = list(entry[2]).count(entry[1])
	if c >= entry[0][0] and c <= entry[0][1]:
		valid += 1

print(valid)
