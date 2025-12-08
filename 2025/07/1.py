from collections import defaultdict


class Spliter:
    all: dict[int, list['Spliter']] = defaultdict(list)

    def __init__(self, rank_y: int, position_x: int):
        self.rank = rank_y
        self.position = position_x
        self._timelines: int | None = None
        self.all[self.position].append(self)

    @classmethod
    def find_next_spliter(cls, rank_y: int, position_x: int) -> 'None | Spliter':
        for spliter in cls.all[position_x]:
            if spliter.rank < rank_y:
                continue
            return spliter
        return None

    def timelines(self) -> int:
        if self._timelines is not None:
            return self._timelines
        self._timelines = 1
        left_spliter = self.find_next_spliter(self.rank + 1, self.position - 1)
        self._timelines += left_spliter.timelines() if left_spliter else 0
        right_spliter = self.find_next_spliter(self.rank + 1, self.position + 1)
        self._timelines += right_spliter.timelines() if right_spliter else 0
        return self._timelines


start = 0

for i, line in enumerate(open('prod.txt')):
    if i == 0:
        start = line.index('S')
        continue
    for c_i, car in enumerate(line):
        if car == '^':
            Spliter(i // 2, c_i)

print(Spliter.find_next_spliter(0, start).timelines() + 1)
