from typing import Iterator, Literal

position = tuple[int, int]
direction = tuple[Literal[-1, 0, 1], Literal[-1, 0, 1]]


class GuardArea:

    def __init__(self, file_name: str):
        self.area: dict[position, str] = {}
        with open(file_name) as f:
            for y, line in enumerate(f):
                line = line.rstrip()
                for x, element in enumerate(line):
                    if element == '^':
                        self.guard_start_position = x, y
                    self.area[x, y] = element

    def guard_steps(self) -> Iterator[tuple[position, direction]]:
        directions: tuple[direction, ...] = ((-1, 0), (0, 1), (1, 0), (0, -1))
        guard_d: direction = directions[3]
        guard_p: position = self.guard_start_position
        while True:
            try:
                while self.area[guard_p[0] + guard_d[0], guard_p[1] + guard_d[1]] == '#':
                    guard_d = directions[directions.index(guard_d) - 1]
                guard_p = guard_p[0] + guard_d[0], guard_p[1] + guard_d[1]
            except KeyError:
                break
            yield guard_p, guard_d


# guard_area = GuardArea('6_exemple.txt')
guard_area = GuardArea('6.txt')


def guard_out() -> int:
    guard_way: set[position] = set()
    for pos, _ in guard_area.guard_steps():
        guard_way.add(pos)
    return len(guard_way)


def guard_loops():
    def is_guard_loop() -> bool:
        guard_way: set[tuple[position, direction]] = set()
        for pos_dir in guard_area.guard_steps():
            if pos_dir in guard_way:
                return True
            guard_way.add(pos_dir)
        else:
            return False

    loops = 0
    for case, element in guard_area.area.items():
        if element != '.':
            continue

        guard_area.area[case] = '#'
        loops += is_guard_loop()
        guard_area.area[case] = '.'
    return loops


print(guard_out())
print(guard_loops())
