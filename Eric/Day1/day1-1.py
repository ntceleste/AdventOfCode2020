f=open('input.txt', 'r')
numbers = [int((line.strip())) for line in f]
f.close()
stop = 0
for i in numbers:
	for y in numbers:
		if i != y and i + y == 2020:
			print('{} * {} = {}'.format(i, y, i*y))
			stop = 1
			break
	if stop:
		break
