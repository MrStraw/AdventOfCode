from itertools import product

rolls = {(x, y) for y, line in enumerate(open('prod.txt')) for x, cell in enumerate(line.strip()) if cell == '@'}


def free_rolls():
    for x, y in rolls.copy():
        if sum((x + a, y + b) in rolls for a, b in set(product((-1, 0, 1), repeat=2)) - {(0, 0)}) < 4:
            yield x, y


print(len(list(free_rolls())))

start, old_rolls = len(rolls), {}
while old_rolls != rolls:
    old_rolls = rolls.copy()
    for x, y in free_rolls():
        rolls.discard((x, y))
print(start - len(rolls))
