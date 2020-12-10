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

print(candidate_index, numbers[candidate_index])
