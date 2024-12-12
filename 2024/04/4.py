import itertools


class Matrice:

    def __init__(self):
        with open('4.txt') as f:
            self.table = [line.rstrip() for line in f]

    def __iter__(self):
        for row_i in range(len(self.table)):
            for column_i in range(len(self.table[row_i])):
                yield column_i, row_i

    def __call__(self, case_x: int, case_y: int):
        if case_x < 0 or case_y < 0:
            return ''
        try:
            return self.table[case_y][case_x]
        except IndexError:
            return ''


matrice = Matrice()


def count_xmas(cell_x: int, cell_y: int) -> int:
    if matrice(cell_x, cell_y) != 'X':
        return 0
    _xmas_count = 0
    for look_x, look_y in set(itertools.product((-1, 0, 1), repeat=2)) - {(0, 0)}:
        string_get = 'X'
        for i in range(1, 4):
            string_get += matrice(cell_x + look_x * i, cell_y + look_y * i)
        _xmas_count += string_get == 'XMAS'
    return _xmas_count


def is_x_mas(cell_x: int, cell_y: int) -> bool:
    if matrice(cell_x, cell_y) != 'A':
        return False
    for dash in (1, -1):
        mas = {'A'}
        mas.add(matrice(cell_x - 1, cell_y - dash))
        mas.add(matrice(cell_x + 1, cell_y + dash))
        if mas != set('MAS'):
            return False
    return True


xmas, x_mas = 0, 0
for cell in matrice:
    xmas += count_xmas(*cell)
    x_mas += is_x_mas(*cell)
print("XMAS:", xmas)
print("X-MAS:", x_mas)
