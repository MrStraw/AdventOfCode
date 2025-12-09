from dataclasses import dataclass
from math import sqrt


@dataclass(unsafe_hash=True)
class Boxe:
    x: int
    y: int
    z: int

    def __repr__(self):
        return f"({self.x},{self.y},{self.z})"

    def __sub__(self, other: 'Boxe'):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)


boxes, distances = set(), set()
for boxe_pos in open('prod.txt'):
    x, y, z = boxe_pos.strip().split(',')
    boxe = Boxe(int(x), int(y), int(z))
    for other_boxe in boxes:
        distances.add((boxe - other_boxe, boxe, other_boxe))
    boxes.add(boxe)
top_distances: list[tuple[float, Boxe, Boxe]] = sorted(distances, key=lambda b: b[0])

len_total = len(boxes)
circuits: dict[Boxe, int] = {}
for i, (_, b1, b2) in enumerate(top_distances, start=1):
    if b1 not in circuits and b2 not in circuits:
        circuits[b1] = circuits[b2] = i
    elif b1 in circuits and b2 not in circuits:
        circuits[b2] = circuits[b1]
    elif b2 in circuits and b1 not in circuits:
        circuits[b1] = circuits[b2]
    elif circuits[b1] != circuits[b2]:
        old_c = circuits[b2]
        for b, c in circuits.items():
            if c == old_c:
                circuits[b] = circuits[b1]
                
    if len_total == len(circuits) and len(set(circuits.values())) == 1:
        print(b1.x * b2.x)
        break