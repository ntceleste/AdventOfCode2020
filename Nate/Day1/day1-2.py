input = open("input.txt").read().split()
numbers = list(map(int, input))

for i in numbers:
    for j in numbers:
            target = 2020 - i - j
            if target in numbers:
                print(target * i * j)
                exit()

