from datetime import datetime
from itertools import count
from operator import is_not


class Stone:
    stones: dict[str, 'Stone'] = {}

    def __new__(cls, mark: str):
        if not isinstance(mark, str):
            raise Exception("int injécté dans l'appel d'une stone")
        if mark not in Stone.stones:
            Stone.stones[mark] = super().__new__(cls)
        return Stone.stones[mark]

    def __init__(self, mark: str):
        if hasattr(self, 'mark'):
            return
        self.mark: str = mark
        self.evolve_register: dict[int, str] = {}
        # self.equivalent: tuple[str, int] | None = self._equivalent
        
    # @property
    # def _equivalent(self) -> tuple[str, int] | None:
    #     minus = int(self.mark)
    #     for i in count(0):
    #         next_minus = minus / 2024
    #         if not next_minus.is_integer():
    #             break
    #         minus = next_minus
    #     if i:
    #         return str(int(minus)), i
    #     return None

    def __repr__(self):
        return f'{self.mark}'

    def __getitem__(self, evolve_time: int) -> str:
        if not evolve_time:
            return self.mark
        # if self.equivalent:
        #     equi = Stone(self.equivalent[0])
        #     equi_rank = equi[self.equivalent[1] + evolve_time]
        #     return equi_rank
        if not evolve_time in self.evolve_register:
            self.evolve_register[evolve_time] = ' '.join(stone.mark for stone in self.evolve())
        return ' '.join(Stone(stone_mark)[evolve_time - 1] for stone_mark in self.evolve_register[evolve_time].split())

    def evolve(self) -> list['Stone']:
        if self.mark == '0':
            return [Stone('1')]

        len_mark = len(str(self.mark))
        if not len_mark % 2:
            mid_mark = len_mark // 2
            return [Stone(self.mark[:mid_mark]), Stone(str(int(self.mark[mid_mark:])))]

        return [Stone(str(int(self.mark) * 2024))]


start = datetime.now()

# arrangement = ' '.join([Stone(mark)[75] for mark in '9759 0 256219 60 1175776 113 6 92833'.split()])
# print(arrangement.count(' ') + 1)
print(Stone('2097446912'))
print(Stone('2097446912')[3])

print(datetime.now() - start)
