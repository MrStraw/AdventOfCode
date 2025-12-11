from itertools import combinations
from scipy.optimize import linprog


a = b = 0
for diagram, *buttons, joltage in map(str.split, open('prod.txt')):
    diagram = [c=='#' for c in diagram[1:-1]]
    buttons = [eval(b[:-1]+',)') for b in buttons]
    joltage = eval(joltage[1:-1])
    numbers = range(len(joltage))

    def toggle(buttons):
        for n in numbers:
            for pressed in combinations(buttons, n):
                lights = [sum(i in p for p in pressed)%2 for i in numbers]
                if lights == diagram: return n

    a += toggle(buttons)

    c = [1 for _ in buttons]
    A = [[i in b for b in buttons] for i in numbers]

    b += linprog(c, A_eq=A, b_eq=joltage, integrality=1).fun

print(a, int(b))