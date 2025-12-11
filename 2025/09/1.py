from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations


@dataclass(unsafe_hash=True, order=True)
class Tile:
    x: int
    y: int

    def __repr__(self):
        return f"({self.x}|{self.y})"

    def __sub__(self, other: 'Tile') -> int:
        return (abs(self.x - other.x) + 1) * (abs(self.y - other.y) + 1)


red_tiles = {
    Tile(int(x), int(y))
    for tiles_pos in open('prod.txt') for x, y in [tiles_pos.strip().split(',')]
}

print(max(t1 - t2 for t1, t2 in combinations(red_tiles, 2)))

# mm, mm_ranges = defaultdict(list), {}
# for t in (sorted(red_tiles, key=lambda _: _.x)):
#     mm[t.x].append(t)
# for z in mm:
#     if len(mm[z]) != 1:
#         a, b = sorted([mm[z][0].y, mm[z][-1].y])
#         mm_ranges[z] = range(a + 1, b)
# 
# lines = red_tiles.copy()
# for x, r in mm_ranges.items():
#     for y in r:
#         lines.add(Tile(x, y))
# lines_by_y: dict[int, list | tuple[int, int]] = defaultdict(list)
# for t in lines:
#     lines_by_y[t.y].append(t.x)
# for y in lines_by_y:
#     s = sorted(lines_by_y[y])
#     lines_by_y[y] = s[0], s[-1]
# 
# max_ = 0
# for t1, t2 in combinations(red_tiles, 2):
#     len_rect = t1 - t2
#     if len_rect < max_:
#         continue
#     for to_check in {Tile(t1.x, t2.y), Tile(t2.x, t1.y)}:
#         line_y = lines_by_y[to_check.y]
#         if not line_y[0] <= to_check.x <= line_y[1]:
#             break
#     else:
#         max_ = len_rect
# print(max_)
# assert max_ < 4630762112
