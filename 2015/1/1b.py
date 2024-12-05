floors_inputs = open('floors.txt').read()
floor = 0
for i, floor_input in enumerate(floors_inputs, start=1):
    match floor_input:
        case '(':
            floor += 1
        case ')':
            floor -= 1
    if floor == -1:
        print(i)
        break
