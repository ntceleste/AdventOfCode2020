input = open('input.txt').read().split("\n")
input.pop()

rules = {}
for line in input:
    line = line.replace(' bags', '').replace(' bag', '').replace('.', '')
    outer, inner = line.split(' contain')
    inner = inner.split(', ')
    items = []
    for bags in inner:
        bags = bags.strip()
        if bags == 'no other':
            bags = { 'number': 0, 'color': bags}
        else:
            number, color = bags.split(' ', 1)
            number = int(number)
            bags = {
                'number': number,
                'color': color.strip()
            }
        items.append(bags)
    rules[outer] = items


def bag_can_contain(items, color):
    for item in items:
        if item['color'] == color:
            return True
        if item['color'] != 'no other':
            if bag_can_contain(rules[item['color']], color):
                return True
    return False


total = 0
for color, items in rules.items():

    if bag_can_contain(items, 'shiny gold'):
        total += 1
        
print(total)
