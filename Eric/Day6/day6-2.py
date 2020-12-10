input = open('input.txt').read().split("\n\n")


def set_of_characters(value):
    return set(list(value))


total = 0
for data in input:
    data = list(map(set_of_characters, data.split()))
    total += len(data[0].intersection(*data[1:]))

print(total)

