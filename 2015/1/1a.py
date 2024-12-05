floors_inputs = open('floors.txt').read()
floor = 0
for floor_input in floors_inputs:
    match floor_input:
        case '(':
            floor += 1
        case ')':
            floor -= 1
print(floor)
