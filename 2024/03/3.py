import re

total = 0
skip = False
for instruction in re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", open('3.txt').read()):
    match instruction:
        case "don't()":
            skip = True
        case "do()":
            skip = False
        case mul:
            if not skip:
                x, y = mul[4:-1].split(',')
                total += int(x) * int(y)

print(format(total, ','))
