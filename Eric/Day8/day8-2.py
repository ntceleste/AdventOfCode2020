input = open('input.txt').read().split("\n")
input.pop() #removes the final empty element

program = input.copy()
trace = []
attempt = 0
end = len(program)
line = 0

while line < end:
    if line == 0:
        visited = []
        accumulator = 0
    if line in visited:
        attempt += 1
        program = input.copy()
        target = trace[len(trace) - attempt]
        original = program[target]
        # print("changing {} '{}'".format(target, original))
        instruction, value = original.split()
        if instruction == 'nop':
            instruction = 'jmp'
        if instruction == 'jmp':
            instruction = 'nop'
        program[target] = '{} {}'.format(instruction, value)
        line = 0
    else:
        visited.append(line)
        instruction, value = program[line].split()
        if instruction == 'acc':
            accumulator += int(value)
            line += 1
        else:
            if not attempt:
                # print('tracing {}'.format(line))
                trace.append(line)
            if instruction == 'jmp':
                line += int(value)
            if instruction == 'nop':
                line += 1



print(accumulator)
