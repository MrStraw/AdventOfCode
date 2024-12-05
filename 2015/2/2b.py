total = 0

with open('dimensions.txt') as f:
    for dimensions in f:
        dimensions = sorted((int(d) for d in dimensions.split('x')))
        total += (dimensions[0] * 2 + dimensions[1] * 2) + (dimensions[0] * dimensions[1] * dimensions[2])

print(total)
