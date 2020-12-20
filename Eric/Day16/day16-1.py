input = open('input.txt').read().split("\n\n")

allowed = set()
rules = input[0].split("\n")
for rule in rules:
    parts = rule.split(': ')
    name = parts[0]
    parts = parts[1].split(' or ')
    nums = [
        parts[0],
        parts[1]
    ]
    for n in nums:
        ok = [ int(e) for e in n.split('-')]
        allowed = allowed | set(range(ok[0], ok[1] + 1))
    print(name, nums)

tickets = input[2].split("\n")
tickets.pop() # remove blank last line
tickets.pop(0) # remove first line label
total = 0
for ticket in tickets:
    elements = [ int(e) for e in ticket.split(',')]
    for el in elements:
        if el not in allowed:
            total += el

print(allowed, rules, tickets, total)
