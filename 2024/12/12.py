from itertools import pairwise

Coord = tuple[int, int]


class Guarden:
    def __init__(self):
        self.plots: dict[Coord, str] = {}
        with open('12.txt') as f:
            for y, row in enumerate(f):
                for x, plant_type in enumerate(row.rstrip()):
                    self.plots[x, y] = plant_type

    def __iter__(self):
        yield from self.plots


guarden = Guarden()


class PlotArrangement:
    all_arrangements: list['PlotArrangement'] = []
    classified: set[Coord] = set()
    look_to = {(0, 1), (0, -1), (1, 0), (-1, 0)}

    def __init__(self, x: int, y: int):
        PlotArrangement.all_arrangements.append(self)
        self.plots: set[Coord] = {(x, y)}
        self.plant_type = guarden.plots[x, y]
        self.fences: set[tuple[float, float]] = set()
        self.__classifie_from_coord(x, y)

    def __str__(self):
        return f"{self.plant_type}: {self.price} ({len(self.plots)}p x {self.sides}s)"

    def __classifie_from_coord(self, x: int, y: int):
        for look_x, look_y in PlotArrangement.look_to:
            coord_look: Coord = x + look_x, y + look_y
            plant_type = guarden.plots.get(coord_look)
            if not plant_type:
                self.fences.add(((x + coord_look[0]) / 2, (y + coord_look[1]) / 2))
                continue
            if coord_look in self.plots:
                continue
            if plant_type != self.plant_type:
                self.fences.add(((x + coord_look[0]) / 2, (y + coord_look[1]) / 2))
                continue
            PlotArrangement.classified.add(coord_look)
            self.plots.add(coord_look)
            self.__classifie_from_coord(*coord_look)

    @property
    def sides(self) -> int:
        axes, sides_ = {}, 0
        for fence_x, fence_y in self.fences:
            f_axe, f_to_check = (fence_y + 0.5, fence_x) if fence_x.is_integer() else (fence_x, fence_y)
            if not f_axe in axes:
                axes[f_axe] = set()
            axes[f_axe].add(f_to_check)
        for axe, fence_to_check in axes.items():
            for f1, f2 in pairwise(sorted(fence_to_check)):
                sides_ += f1 + 1 != f2 or all(
                    ((f1 + 0.5, (axe - 0.5 if axe.is_integer() else axe) + _) in self.fences) for _ in (-0.5, 0.5))

        return sides_ + len(axes)

    @property
    def price(self) -> int:
        return self.sides * len(self.plots)


for coord in guarden:
    if coord not in PlotArrangement.classified:
        PlotArrangement(*coord)

total_prices = 0
for pl in PlotArrangement.all_arrangements:
    if pl.plant_type != 'J':
        continue
    print(pl)
    total_prices += pl.price
print(total_prices)
