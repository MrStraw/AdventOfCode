import itertools
from typing import Iterator


def possibilities(numbers: list[int]) -> Iterator[int]:
    def to_str_to_solve() -> Iterator[list[int | str]]:
        for operators_combinaison in itertools.product('+*|', repeat=len(numbers) - 1):
            nbs = iter(numbers)
            to_solve = [next(nbs)]
            for op in operators_combinaison:
                to_solve += [op, next(nbs)]
            yield to_solve

    def resolve(instructions: list[int | str]):
        instructions = iter(instructions)
        result = next(instructions)
        for instruction in instructions:
            int_ = next(instructions)
            match instruction:
                case '*':
                    result *= int_
                case '+':
                    result += int_
                case '|':
                    result = int(str(result) + str(int_))

        return result

    for to_resolve_ in to_str_to_solve():
        yield resolve(to_resolve_)


total = 0
with open('7.txt') as f:
    # for line in ['156: 15 6']:
    for line in f:
        goal, *numbers_ = [int(i) for i in line.replace(':', '').split()]
        for possibilitie in possibilities(numbers_):
            if goal == possibilitie:
                total += goal
                break

print(total)  # 159490400628354
