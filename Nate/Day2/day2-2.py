import re
input = open("input.txt").read().split('\n')

valid_count = 0

for password_set in input:
    password_rule = password_set.split(':')[0]
    password = password_set.split(':')[1].strip()
    first = list(map(int, re.findall(r'\d+', password_rule)))[0] - 1
    second = list(map(int, re.findall(r'\d+', password_rule)))[1] - 1
    char = list(re.findall(r'\D+', password_rule))[1].strip()
    
    if password[first] != password[second]:
        if password[first] == char or password[second] == char: 
            valid_count += 1

print(valid_count)
