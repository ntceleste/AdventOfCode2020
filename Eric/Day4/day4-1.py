input = open('input.txt').read().split("\n\n")

needles = [
	'byr:',
	'iyr:',
	'eyr:',
	'hgt:',
	'hcl:',
	'ecl:',
	'pid:'
	]
	
valid = 0
for data in input:
	passport = True
	for needle in needles:
		if needle not in data:
			passport = False
			break
	if passport:
		valid += 1

print(valid)

