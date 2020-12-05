import re
input = open("input.txt").read().split('\n')

valid_count = 0

for password_set in input:
    password_rule = password_set.split(':')[0]
    password = password_set.split(':')[1]
    min = list(map(int, re.findall(r'\d+', password_rule)))[0]
    max = list(map(int, re.findall(r'\d+', password_rule)))[1]
    char = list(re.findall(r'\D+', password_rule))[1].strip()

    letter_count = 0
    for letter in password:
        if letter == char:
            letter_count += 1 
    
    if letter_count >= min and letter_count <= max:
        valid_count += 1

print(valid_count)
