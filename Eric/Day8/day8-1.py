input = open('input.txt').read().split("\n")
input.pop() #removes the final empty element

visited = []
accumulator = 0
end = len(input)

def execute(line):
    global accumulator
    if line < end and line not in visited:
        visited.append(line)
        instruction, value = input[line].split()
        if instruction == 'acc':
            accumulator += int(value)
            execute(line + 1)
        if instruction == 'jmp':
            execute(line + int(value))
        if instruction == 'nop':
            execute(line + 1)
    return


execute(0)
print(accumulator)
