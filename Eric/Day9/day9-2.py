input = open('input.txt').read().split()
preamble = 25
numbers = list(map(int, input))

target_index = preamble

while target_index < len(numbers):
    target = numbers[target_index]
    candidate_index = target_index - preamble
    while candidate_index < target_index:
        # should be the sum of any two
        goal = target - numbers[candidate_index]
        if goal == target:
            # the two numbers will have different values
            candidate_index += 1
            continue
        try:
            # of the 25 immediately previous numbers
            goal_index = numbers.index(goal, target_index - preamble, target_index - 1)
            break
        except:
            # not found
            candidate_index += 1
            continue
    if candidate_index == target_index:
        break
    target_index += 1

goal = numbers[candidate_index]
print(candidate_index, goal)

candidates = []
found = []
for number in numbers:
    drop = []
    candidate_index = 0
    for candidate in candidates:
        candidate.append(number)
        total = sum(candidate)
        if total == goal:
            found = candidate
            break
        if total > goal:
            drop.append(candidate_index)
        candidate_index += 1
    if found:
        break
    candidates.append([number])
    
    
print(candidate)
candidate.sort()
print(candidate[0] + candidate.pop())
