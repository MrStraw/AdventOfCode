import itertools

all_distances = {}
places = set()

with open('9.txt') as f:
    for line in f:
        infos = line.split()
        all_distances[frozenset((infos[0], infos[2]))] = int(infos[4])
        places.add(infos[0])
        places.add(infos[2])

print(f"{len(places)} places à visiter")

ways = set()
for way in itertools.permutations(places, len(places)):
    if tuple(reversed(way)) in ways:
        continue
    ways.add(way)
print(f"{len(ways)} combinaisons à tester")

min_distance = 0
max_distance = 0
for way in ways:
    len_way = sum(all_distances[frozenset((way[i], way[i + 1]))] for i in range(len(way) - 1))
    if not min_distance or min_distance > len_way:
        min_distance = len_way
    if max_distance < len_way:
        max_distance = len_way

print(min_distance)
print(max_distance)
