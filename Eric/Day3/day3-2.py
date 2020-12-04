from functools import reduce

slopes = [
		[1, 1],
		[3, 1],
		[5, 1],
		[7, 1],
		[1, 2]
	]

lines = open('input.txt').read().split("\n")
hill = list(map(list, lines))
hill.pop()
width = len(hill[0])

def trees4slope(slope):
	trees = 0
	step = 0
	
	for i in range(0, len(hill), slope[1]):
		level = hill[i]
		position = (step * slope[0]) % width
		if level[position] == '#':
			trees += 1
		step += 1
	
	return trees

print(reduce((lambda x, y: x * y), list(map(trees4slope, slopes))))
