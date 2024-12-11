from typing import Iterable


class Cell:
    __all_cells_pos: dict[tuple[int, int], 'Cell'] = {}
    __directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}

    def __new__(cls, x: int, y: int, level: int = None):
        match level is not None, (pos := (x, y)) in cls.__all_cells_pos:
            case False, True:
                pass
            case False, False:
                return None
            case True, False:
                cls.__all_cells_pos[pos] = super().__new__(cls)
        return cls.__all_cells_pos[pos]

    def __init__(self, x: int, y: int, level: int = None):
        if hasattr(self, 'level'):
            return
        self.x = x
        self.y = y
        self.level = level

    @property
    def next_cells(self) -> set['Cell']:
        next_cells_ = set()
        if self.level == 9:
            return next_cells_
        for look_x, look_y in Cell.__directions:
            look_cell = Cell(self.x + look_x, self.y + look_y)
            if look_cell and look_cell.level == self.level + 1:
                next_cells_.add(look_cell)
        return next_cells_

    def propage(self):
        cells = [self]
        way_continue = True
        while way_continue:
            way_continue = False
            new_cells = []
            for cell in cells:
                next_cells = cell.next_cells
                if next_cells:
                    way_continue = True
                    new_cells += [next_cell for next_cell in cell.next_cells]
                elif cell.level == 9:
                    new_cells.append(cell)
            cells = new_cells
        return cells


class LavaMap:

    def __init__(self):
        self.all_cells = set()
        self.start_cells = set()
        with open('10.txt') as f:
            for y, row in enumerate(f):
                for x, level in enumerate(row.rstrip()):
                    self.all_cells.add(Cell(x, y, int(level)))
                    if level == '0':
                        self.start_cells.add(Cell(x, y))

    # def continue_ways(self, ways: Iterable[list[Cell]]) -> list[list[Cell]]:
    #     updates_ways: list[list[Cell]] = []
    # 
    #     for way_ in ways:
    #         last_cell = way_[-1]
    #         next_cells = last_cell.next_cells
    #         if next_cells:
    #             updates_ways += [[*way_, next_cell] for next_cell in next_cells]
    #         elif last_cell.level == 9:
    #             updates_ways.append(way_)
    # 
    #     if any(way_[-1].next_cells for way_ in updates_ways):
    #         updates_ways = self.continue_ways(updates_ways)
    #     return updates_ways


lava_map = LavaMap()
print(sum(len(cell.propage()) for cell in lava_map.start_cells))
