rows = [line.strip('\n') for line in open('prod.txt')]
instructions = zip(*reversed(rows))

math_chunk = ''
total = 0
chunk = []
for col in instructions:
    if col[0] in '+*':
        math_chunk = col[0]
    if set(col) != {' '}:
        chunk.append(''.join(reversed(col[1:])))
    else:
        total += eval(math_chunk.join(chunk))
        chunk = []
total += eval(math_chunk.join(chunk))
print(total)