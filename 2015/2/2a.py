total = 0

with open('dimensions.txt') as f:
    for dimensions in f:
        l, w, h = (int(d) for d in dimensions.split('x'))
        total += 2*l*w + 2*w*h + 2*h*l + min(l*w, l*h, w*h)

print(total)
