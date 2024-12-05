pos = 0, 0
pos_histo = {pos}

for direction in open('directions.txt').read():
    match direction:
        case '<':
            pos = pos[0] - 1, pos[1]
        case '>':
            pos = pos[0] + 1, pos[1]
        case '^':
            pos = pos[0], pos[1] + 1
        case 'v':
            pos = pos[0], pos[1] - 1
    pos_histo.add(pos)

print(len(pos_histo))
