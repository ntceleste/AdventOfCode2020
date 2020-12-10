input = open('input.txt').read().split()
numbers = list(map(int, input))
numbers.sort()

# print(numbers)

diffs = {
    1: 0,
    2: 0,
    3: 1
}
previous = 0
for number in numbers:
    diff = number - previous
    diffs[diff] += 1
    previous = number

print(diffs, diffs[1] * diffs[3])

