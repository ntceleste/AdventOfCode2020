import re
input = open('input.txt').read().split("\n\n")
rules = {}
for rule in input[0].splitlines():
    rule_parts = rule.split(":")
    rule_index = int(rule_parts[0])
    rules[rule_index] = rule_parts[1].replace("\"", "").strip()

data = []
for d in input[1].splitlines():
    data.append(d)

answer = 0
lookup = {}
for i in rules:
    if rules[i].isalpha():
        lookup[i] = rules[i]

while True:
    for i in rules:
        complete = True
        rule_parts = rules[i].split()
        for r_part in rule_parts:
            if r_part.isdigit():
                complete = False
                int_r_part = int(r_part)
                if int_r_part in lookup:
                    rules[i] = re.sub(
                        f"\\b{r_part}\\b", f"(?:{lookup[int_r_part]})", rules[i])

        if complete and i not in lookup:
            rules[i] = rules[i].replace(" ", "")
            lookup[i] = rules[i]

    if 0 in lookup:
        break

for d in data:
    answer += bool(re.match(f'^{lookup[0]}$', d))

print("Lines matching rule[0]: " + str(answer))
