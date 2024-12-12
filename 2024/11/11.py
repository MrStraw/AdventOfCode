from datetime import datetime
from pprint import pprint
from typing import Iterator


class Stone:
    stones: dict[int, 'Stone'] = {}

    def __new__(cls, rune: int):
        if rune not in Stone.stones:
            Stone.stones[rune] = super().__new__(cls)
        return Stone.stones[rune]

    def __init__(self, rune: int):
        if hasattr(self, 'rune'):
            return
        self.rune: int = rune
        self.evolve_register: dict[int, int] = {}

    # def __repr__(self):
    #     return f'S:{self.rune}'

    def __getitem__(self, blinks: int) -> int:
        if not blinks:
            return 1
        if blinks not in self.evolve_register:
            i = 0
            for next_stone in self.evolve():
                i += next_stone[blinks - 1]
            self.evolve_register[blinks] = i
        return self.evolve_register[blinks]

    def evolve(self) -> Iterator['Stone']:
        if not self.rune:
            yield Stone(1)
        elif not (len_mark := len(str(self.rune))) % 2:
            mid_rune = len_mark // 2
            yield Stone(int(str(self.rune)[:mid_rune]))
            yield Stone(int(str(self.rune)[mid_rune:]))
        else:
            yield Stone(self.rune * 2024)


start = datetime.now()

stones_start = (9759, 0, 256219, 60, 1175776, 113, 6, 92833)
total = sum(Stone(number_stones)[75] for number_stones in stones_start)
print(total)

print(datetime.now() - start)  # 0:00:00.140838
