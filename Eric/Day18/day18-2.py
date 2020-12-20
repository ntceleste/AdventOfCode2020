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


# We have 2 rules:
#   - literals always goes to the output stack
#   - when an operator with lower or equal precedence 
#     than the last element of the operators stack is comming, 
#     pop the last element of the operators stack to the output stack

total = 0
for equation in input:
    out = []
    op = []
    tokens = equation.replace('(', '( ').replace(')', ' )').split()
    # print(tokens)
    while tokens:
        token = tokens.pop(0)
        try:
            # literals always goes to the output stack
            n = int(token)
            out.append(n)
        except:
            # open paren goes to op stack
            # close paren unwinds op stack to last open paren
            if token == '(':
                op.append(token)
            elif token == ')':
                t = op.pop()
                while t != '(':
                    out.append(t)
                    t = op.pop()
            # when an operator with lower or equal precedence 
            # than the last element of the operators stack is comming, 
            # pop the last element of the operators stack 
            # to the output stack
            # addition is higher precedence
            else:
                if op:
                    last_op = op[len(op) - 1]
                    if last_op == '+' or last_op == token:
                        out.append(op.pop())
                op.append(token)
    while op:
        out.append(op.pop())
    
    while len(out) > 1:
        # print(out)
        for i in range(len(out)):
            t = out[i]
            if t == '*' or t == '+':
                t = out.pop(i)
                r = out.pop(i - 1)
                l = out[i - 2]
                if t == '+':
                    out[i - 2] = l + r
                else:
                    out[i - 2] = l * r
                break
    
    value = out[0]
    print(value)
    total += value
    
print(total)
