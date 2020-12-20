input = open('practice.txt').read().split("\n\n")
rules_unparsed = input[0].split('\n')
messages = input[1].split('\n')
blank_line = messages.pop()

rules = {}
for r in rules_unparsed:
    (key, value) = r.split(': ')
    values_unparsed = value.replace('"', '').split(' | ')
    lookups = []
    value = None
    for i in range(len(values_unparsed)):
        lookups.append([])
        for val in values_unparsed[i].split():
            try:
                lookups[i].append(int(val))
            except:
                lookups = None
                value = val
                break
    rules[int(key)] = {
        'lookups': lookups,
        'value': value
    }


def resolve_rule(inrule):
    global rules
    rule = rules[inrule]
    values = []
    
    if rule['value']:
        values.append(rule['value'])
        
    elif rule['lookups']:
        values = []
        for lookup in rule['lookups']:
            before = ['']
            for subrule in lookup:
                after = []
                resolved = resolve_rule(subrule)
                for addition in resolved:
                    for already in before:
                        after.append(already + addition)
                before = after
                
            for newval in before:
                if newval not in values:
                    values.append(newval)
    
    return values

candidates = resolve_rule(0)

# print(rules, '\n\ncandidates =', candidates, '\n\nmessages = ', messages)

total = 0
for message in messages:
    if message in candidates:
        total += 1

print(total)
