input = open('input.txt').read().split()
numbers = list(map(int, input))

index = 0
used = []
for i in numbers:
	needle = 2020 - i
	try:
		found = numbers.index(needle)
		solution = i * needle
		if found != index and (solution not in used):
			used.append(solution)
			print('{} * {} = {}'.format(i, needle, i * needle))
	except:
		pass
	index += 1

