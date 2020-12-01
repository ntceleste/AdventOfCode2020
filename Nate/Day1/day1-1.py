
input = open("input.txt")
inputLines = input.read().split()
numbers = list(map(int, inputLines))

for i in numbers:
    target = 2020 - i
    if target in numbers:
        print(target * i)
        exit()
