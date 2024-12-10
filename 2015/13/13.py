import itertools

interactions: dict[frozenset[str, str]: int] = {}
guests: set[str] = set()

with open('13.txt') as f:
    for line in f:
        line = line.rstrip('\n.').split()
        happiness = int(line[3]) * (-1 if line[2] == 'lose' else 1)
        if (couple := frozenset({line[0], line[10]})) in interactions:
            interactions[couple] += happiness
        else:
            interactions[couple] = happiness
        guests.add(line[0])

best_arrangement = 0
for arrangement in itertools.permutations(guests | {'me'}):
    arrangement_happiness = 0
    for couple in itertools.pairwise((*arrangement, arrangement[0])):
        if 'me' not in couple:
            arrangement_happiness += interactions[frozenset(couple)]
    best_arrangement = max(arrangement_happiness, best_arrangement)

print(best_arrangement)
