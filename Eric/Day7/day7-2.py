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


def bags_contained(color):
    total = 0
    for item in rules[color]:
        total += item['number']
        if item['color'] != 'no other':
            total += bags_contained(item['color']) * item['number']
    return total


total = bags_contained('shiny gold')
print(total)
