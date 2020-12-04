import re
input = open('input.txt').read().split("\n\n")

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
def birthyear(value):
	try:
		value = int(value)
	except:
		return False
	return 1920 <= value <= 2002

# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
def issueyear(value):
	try:
		value = int(value)
	except:
		return False
	return 2010 <= value <= 2020

# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
def expirationyear(value):
	try:
		value = int(value)
	except:
		return False
	return 2020 <= value <= 2030

# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
def height(value):
	m = re.match(r"(\d+)(\w+)", value)
	if m:
		try:
			value = int(m.group(1))
		except:
			return False
		if m.group(2) == 'cm':
			return 150 <= value <= 193
		if m.group(2) == 'in':
			return 59 <= value <= 76
	return False

# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
def haircolor(value):
	m = re.match(r"^#[0-9a-f]{6}$", value)
	return bool(m)

# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
def eyecolor(value):
	return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	
# pid (Passport ID) - a nine-digit number, including leading zeroes.
def passportid(value):
	m = re.match(r"^[0-9]{9}$", value)
	return bool(m)

# cid (Country ID) - ignored, missing or not.
def skip(value):
	return True
	
switcher = {
	'byr': birthyear,
	'iyr': issueyear,
	'eyr': expirationyear,
	'hgt': height,
	'hcl': haircolor,
	'ecl': eyecolor,
	'pid': passportid
	}

valid = 0
for data in input:
	passport = True
	data = data.replace("\n", ' ').split(' ')
	record = {}
	for item in data:
		if item == '':
			continue
		key, value = item.split(':')
		record[key] = value
	for key, test in switcher.items():
		if key not in record or test(record[key]) != True:
			passport = False
			break
	if passport:
		valid += 1

print(valid)
