input = open('input.txt').read().split("\n")
blank_line = input.pop()


def calc():
    global tokens
    total = 0
    op = ''
    while True:
        if tokens == []:
            return total
        token = tokens.pop(0)
        if token == ')':
            return total
        if token == '(':
            token = calc()
        try:
            n = int(token)
            if op:
                if op == '+':
                    total += n
                if op == '*':
                    total *= n
                op = ''
            else:
                total = n
        except:
            op = token        


tokens = []
total = 0
for equation in input:
    tokens = equation.replace('(', '( ').replace(')', ' )').split()
    # print(tokens)
    value = calc()
    print(value)
    total += value
    
print(total)
