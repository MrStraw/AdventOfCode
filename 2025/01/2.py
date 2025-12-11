position, clics = 50, 0
for instructions in open('prod.txt'):
    raw_next_pos = position + int(instructions.replace('L', '-').strip('R\n'))
    clics += abs(raw_next_pos) // 100 + bool(position) if raw_next_pos <= 0 else raw_next_pos // 100
    position = raw_next_pos % 100
