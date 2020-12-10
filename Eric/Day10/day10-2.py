input = open('input.txt').read().split()
numbers = list(map(int, input))
numbers.sort()
numbers.insert(0, 0)
last = numbers.pop()
numbers.append(last)
numbers.append(last + 3)

# print(numbers)

options = []
previous = 0
i = 0
end = len(numbers) - 1  # index of last element in numbers
for i in range(len(numbers)):
    number = numbers[i]
    paths = []
    # we could step to the next element if it exists
    if i < end:
        paths.append(i + 1)
    # we could skip the next element if the one after
    # is less than three away
    if (i + 1) < end:
        diff = numbers[i + 2] - number
        if diff <= 3:
            paths.append(i + 2)
    # and we could skip two elements if the third
    # is less than three away
    if (i + 2) < end:
        diff = numbers[i + 3] - number
        if diff <= 3:
            paths.append(i + 3)
    options.append(paths)

# create a counts array filled with zeros
counts = [0 for i in range(len(options))]
# put the number 1 into the last element of counts
counts[len(counts) - 1] = 1
# working backwards through the options
# but skipping the last element
# find the count for each option
# working backwards so that the counts are
# filled in before they are used below
for i in range(len(options) - 2, -1, -1):
    count = 0
    for option in options[i]:
        count += counts[option]
    counts[i] = count
    # print(i, options[i], numbers[i], count)


print(counts[0])
