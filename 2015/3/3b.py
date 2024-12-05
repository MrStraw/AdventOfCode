pos_santa, pos_robot = [0, 0], [0, 0]
pos_histo = {(0, 0)}


def moove(position: list[int, int], direction: str):
    match direction:
        case '<':
            position[0] -= 1
        case '>':
            position[0] += 1
        case '^':
            position[1] += 1
        case 'v':
            position[1] -= 1
    pos_histo.add(tuple(position))


for i, dir_input in enumerate(open('directions.txt').read()):
    if i % 2:
        moove(pos_robot, dir_input)
    else:
        moove(pos_santa, dir_input)

print(len(pos_histo))
