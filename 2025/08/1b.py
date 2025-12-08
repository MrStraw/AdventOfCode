from collections import defaultdict
from dataclasses import dataclass
from math import sqrt

@dataclass
class Boxe:
    x: int
    y: int
    z: int
    circuit_id: float = None
    
    def __sub__(self, other: 'Boxe'):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)
        

boxes, distances = [], []
for boxe_pos in open('prod.txt'):
    x, y, z = boxe_pos.strip().split(',')
    boxe = Boxe(int(x), int(y), int(z))
    for other_boxe in boxes:
        distances.append((boxe - other_boxe, boxe, other_boxe))
    boxes.append(boxe)
sorted_distances: list[tuple[float, Boxe, Boxe]] = sorted(distances, key=lambda b: b[0])

circuits: dict[float, list[Boxe]] = defaultdict(list)
for i, (_, b1, b2) in enumerate(sorted_distances):
    if i == 11:
        break
    if b1.circuit_id and b2.circuit_id:
        if b1.circuit_id == b2.circuit_id:
            continue
        else:
            for b in circuits[b2.circuit_id]:
                b.circuit_id = b1.circuit_id
                circuits[b1.circuit_id].append(b)
            del circuits[b2.circuit_id]
    if b1.circuit_id:
        b2.circuit_id = b1.circuit_id
        circuits[b2.circuit_id].append(b2)
        continue
    if b2.circuit_id:
        b1.circuit_id = b2.circuit_id
        circuits[b1.circuit_id].append(b1)
        continue
    new_circuit_id = distance
    b1.circuit_id = b2.circuit_id = new_circuit_id
    circuits[new_circuit_id].extend([b1, b2])
    

print(circuits)
top_circuit = dict(sorted(circuits.items(), reverse=True, key=lambda b_: len(b_[1])))
for i, c in enumerate(top_circuit.values()):
    if i == 3:
        break
    print(len(c))