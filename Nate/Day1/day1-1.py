input = open("input.txt").read().split()
numbers = list(map(int, input))


for i in numbers:
    target = 2020 - i
    if target in numbers:
        print(target * i)
        exit()
