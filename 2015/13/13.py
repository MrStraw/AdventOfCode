import itertools

interactions: dict[frozenset[str, str]: int] = {}
guests: set[str] = set()

with open('13.txt') as f:
    for line in f:
        line = line.rstrip('\n.').split()
        happiness = int(line[3]) * (-1 if line[2] == 'lose' else 1)
        if (neighbors := frozenset({line[0], line[10]})) in interactions:
            interactions[neighbors] += happiness
        else:
            interactions[neighbors] = happiness
        guests.add(line[0])

best_arrangement = 0
for arrangement in itertools.permutations(guests | {'me'}):
    best_arrangement = max(
        sum(interactions[frozenset(n)] for n in itertools.pairwise((*arrangement, arrangement[0])) if 'me' not in n),
        best_arrangement
    )

print(best_arrangement)
