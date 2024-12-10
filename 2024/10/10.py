position = tuple[int, int]


class LavaMap:

    def __init__(self):
        self.cells_levels: dict[position, int] = {}
        with open('10.txt') as f:
            for y, row in enumerate(f):
                for x, level in enumerate(row.rstrip()):
                    if level == '.':
                        continue
                    self.cells_levels[x, y] = int(level)

    def search_ways(self, pos: position):
        pos_searched: set[position] = set()
        pos_in_way: set[position] = {pos}
        poss_to_search: set[position] = {pos}

        while poss_to_search:
            print("Des cases sont à fouiller :")
            for to_search in poss_to_search.copy():
                print('-', to_search)
                for look_x, look_y in {(0, 1), (0, -1), (1, 0), (-1, 0)}:
                    pos_search = (to_search[0] + look_x, to_search[1] + look_y)
                    if pos_search in self.cells_levels and pos_searched not in pos_searched:
                        pos_searched.add(pos_search)
                        level_of_search = self.cells_levels[pos_search]
                        if level_of_search == self.cells_levels[to_search] + 1:
                            pos_in_way.add(pos_search)
                            print(pos_search, "ajouté au way")
                            poss_to_search.add(pos_search)
                        # else:
                            # print(pos_search, "rejeté")
                poss_to_search.remove(to_search)

        return pos_in_way


lava_map = LavaMap()
total_score = 0
for pos_0, lvl in lava_map.cells_levels.items():
    if lvl:
        continue
    way = lava_map.search_ways(pos_0)
    for pos_9 in way:
        if lava_map.cells_levels[pos_9] == 9:
            total_score += 1
print(total_score)
