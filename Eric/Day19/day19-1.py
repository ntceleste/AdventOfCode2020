input = open('practice.txt').read().split("\n\n")
rules_unparsed = input[0].split('\n')
messages = input[1].split('\n')
blank_line = messages.pop()

rules = {}
for r in rules_unparsed:
    (key, value) = r.split(': ')
    values_unparsed = value.replace('"', '').split(' | ')
    lookups = []
    valid = []
    unknowns = set([])
    for i in range(len(values_unparsed)):
        lookups.append([])
        for val in values_unparsed[i].split():
            try:
                val = int(val)
                lookups[i].append(val)
                unknowns.add(val)
            except:
                valid = [val]
    rules[int(key)] = {
        'lookups': lookups,
        'valid': valid,
        'unknowns': unknowns
    }


def resolve_rule(inrule):
    global rules
    while not rules[inrule]['valid']:
        for key, rule in rules.items():
            # skip if we've already resolved this one
            if rule['valid']:
                continue
            # check to see if there are any uknowns left
            for unknown in list(rule['unknowns']):
                if rules[unknown]['valid']:
                    rule['unknowns'].remove(unknown)
            if rule['unknowns']:
                continue
            # once we know there are no more unknowns
            # put together the valid message
            lookups = rule['lookups']
            print('resolving {} rules   {}'.format(key, lookups))
            for lookup_index in range(len(lookups)):
                lookup = lookups[lookup_index]
                newlookup = []
                valid_for_lookup = [rules[item]['valid'] for item in lookup]
                print('index {} valid for lookup {}'.format(
                    lookup_index, valid_for_lookup))
                lookup_indexes = range(len(lookup))
                variations = set([])
                for outer_index in lookup_indexes:
                    for inner_index in lookup_indexes:
                        if inner_index == outer_index:
                            continue
                        variations.add(
                            ''.join(valid_for_lookup[outer_index] + valid_for_lookup[inner_index]))
                print('index {} variations {}'.format(lookup_index, variations))
                for item in lookup:
                    valid_for_item = rules[item]['valid']
                    print('index {} item {} valid {}'.format(
                        lookup_index, item, valid_for_item))
                    for val in valid_for_item:
                        newlookup.append(val)
                lookups[lookup_index] = newlookup
            print('resolving {} lookups {}'.format(key, lookups))
            for lookup in lookups:
                rule['valid'].append(''.join(lookup))
            print('resolving {} valid   {}'.format(key, rule['valid']))

    print('values = ', rules[inrule]['valid'])

    x = [
        [
            ['a'], [
                [
                    [
                        [
                            ['a'], ['a']
                        ], [
                            ['b'], ['b']
                        ]
                    ], [
                        [
                            ['a'], ['b']
                        ], [
                            ['b'], ['a']
                        ]
                    ]
                ], [
                    [
                        [
                            ['a'], ['b']
                        ], [
                            ['b'], ['a']
                        ]
                    ], [
                        [
                            ['a'], ['a']
                        ], [
                            ['b'], ['b']
                        ]
                    ]
                ]
            ], ['b']
        ]
    ]

    return []


# print(rules)
candidates = resolve_rule(0)

# print('\n\ncandidates =', candidates, '\n\nmessages = ', messages)

total = 0
for message in messages:
    if message in candidates:
        total += 1

print(total)
