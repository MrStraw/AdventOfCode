rows = [[v for v in line.strip().split(' ') if v] for line in open('prod.txt')]
instructions = zip(*reversed(rows))

total = 0
for car_math, *values in instructions:
    total += eval(car_math.join(values))
print(total)

