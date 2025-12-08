from collections import defaultdict


class Spliter:
    by_pos: dict[int, list['Spliter']] = defaultdict(list)

    def __init__(self, rank_y: int, position_x: int):
        self.rank = rank_y
        self.position = position_x
        self._timelines: int = 0
        self.by_pos[self.position].append(self)

    @classmethod
    def find_next(cls, rank_y: int, position_x: int) -> 'None | Spliter':
        for spliter in cls.by_pos[position_x]:
            if spliter.rank < rank_y:
                continue
            return spliter
        return None

    @property
    def timelines(self) -> int:
        if not self._timelines:
            l_s, r_s = self.find_next(self.rank, self.position - 1), self.find_next(self.rank, self.position + 1)
            self._timelines += (r_s.timelines if r_s else 0) + (l_s.timelines if l_s else 0) + 1
        return self._timelines


start = -1
for i, line in enumerate(open('prod.txt')):
    if i == 0:
        start = line.index('S')
        continue
    for c_i, car in enumerate(line):
        if car == '^':
            Spliter(i, c_i)
print(Spliter.find_next(0, start).timelines + 1)
