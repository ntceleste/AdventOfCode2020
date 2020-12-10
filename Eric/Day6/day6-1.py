import numpy as np
input = open('input.txt').read().split("\n\n")

total = 0
for data in input:
    data = np.unique(list(data.replace("\n", '')))
    total += len(data)

print(total)
