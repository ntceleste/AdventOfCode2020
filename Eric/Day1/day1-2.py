input = open('input.txt').read().split()
numbers = list(map(int, input))

index = 0
used = []
for i in numbers:
	yndex = 0
	for y in numbers:
		needle = 2020 - i - y
		try:
			found = numbers.index(needle)
			solution = i * y * needle
			if found != index and found != yndex and index != yndex and solution not in used:
				used.append(solution)
				print('{} * {} * {} = {}'.format(i, y, needle, i * y * needle))
		except:
			pass
		yndex += 1
	index += 1

