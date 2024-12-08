import itertools

coord = tuple[int, int]

antennas_types: dict[str, set[coord]] = {}
all_antennas_pos: set[coord] = set()
with open('8.txt') as f:
    for y, line in enumerate(f):
        line = line.rstrip()
        for x, ant_type in enumerate(line):
            if ant_type == '.':
                continue
            elif ant_type not in antennas_types:
                antennas_types[ant_type] = set()
            antennas_types[ant_type].add((x, y))
            all_antennas_pos.add((x, y))
map_len = x, y


def calcul_antinodes() -> set[coord]:
    all_antis = set()
    for antennas_pos in antennas_types.values():
        for ant_a, ant_b in itertools.product(antennas_pos, repeat=2):
            if ant_a is ant_b:
                continue
            for wave in itertools.count(1):
                anti_x, anti_y = (ant_a[c] + (ant_a[c] - ant_b[c]) * wave for c in (0, 1))
                if not (0 <= anti_x <= map_len[0]) or not (0 <= anti_y <= map_len[1]):
                    break
                all_antis.add((anti_x, anti_y))
    return all_antis | all_antennas_pos


print(len(calcul_antinodes()))
