f=open('input.txt', 'r')
numbers = [int((line.strip())) for line in f]
f.close()
stop = 0
for i in numbers:
	for y in numbers:
		for z in numbers:
			if i != y and y != z and  i + y + z == 2020:
				print('{} * {} * {} = {}'.format(i, y, z, i*y*z))
				stop = 1
				break
			if stop:
				break
	if stop:
		break
