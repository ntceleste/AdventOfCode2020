input = open("input.txt")
inputLines = input.read().split()
print(inputLines[3])

for i in inputLines:
    for j in inputLines:
        if ((int(i) + int(j)) == 2020):
            print(int(i) * int(j))
