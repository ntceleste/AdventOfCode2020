lines = open('input.txt').read().split("\n")
hill = list(map(list, lines))
hill.pop()

trees = 0
step = 0
width = len(hill[0])

for level in hill:
	position = (step * 3) % width
	if level[position] == '#':
		trees += 1
	step += 1
		
print(trees)
