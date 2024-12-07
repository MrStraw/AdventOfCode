import itertools


def can_be_calibrate(goal: int, numbers: list[int]) -> bool:
    for operators_combinaison in itertools.product('+*|', repeat=len(numbers) - 1):
        nbs = iter(numbers)
        result = next(nbs)
        for op in operators_combinaison:
            match op:
                case '*':
                    result *= next(nbs)
                case '+':
                    result += next(nbs)
                case '|':
                    result = int(str(result) + str(next(nbs)))

        if result == goal:
            return True
    return False


total = 0
with open('7.txt') as f:
    for line in f:
        goal_, *numbers_ = [int(i) for i in line.replace(':', '').split()]
        if can_be_calibrate(goal_, numbers_):
            total += goal_

print(total)
