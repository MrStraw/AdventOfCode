from dataclasses import dataclass, field
from math import sqrt
from typing import ClassVar


@dataclass
class Boxe:
    all: ClassVar[list['Boxe']] = []
    x: int
    y: int
    z: int
    circuit: 'Circuit' = field(default=None, repr=False)
    closest: 'Boxe' = field(default=None, repr=False)

    def __post_init__(self):
        self.all.append(self)
        
    def __str__(self) -> str:
        return f'({self.x},{self.y},{self.z})'
    
    def __lt__(self, other):
        return True

    def find_closest(self) -> float:
        closest_dist = float('inf')
        for box in self.all:
            if box is self:
                continue
            dist = sqrt((self.x - box.x) ** 2 + (self.y - box.y) ** 2 + (self.z - box.z) ** 2)
            if dist < closest_dist:
                closest_dist = dist
                self.closest = box
        return closest_dist


@dataclass
class Circuit:
    all: ClassVar[list['Circuit']] = []
    boxes: list[Boxe] = field(default_factory=list)

    def __post_init__(self):
        self.all.append(self)
        
    def __str__(self):
        return f"{len(self)}: {' - '.join(str(b) for b in self.boxes)}"
        
    def __len__(self):
        return len(self.boxes)
    
    def __lt__(self, other):
        return len(self) < len(other)
    
    def __contains__(self, boxe: Boxe):
        return boxe in self.boxes
    
    def add(self, boxe: Boxe):
        if not boxe.circuit:
            boxe.circuit = self
            self.boxes.append(boxe)
        

    @classmethod
    def join_or_create(cls, boxe: Boxe) -> 'Circuit':
        for c_add in cls.all:
            if boxe.closest in c_add and boxe in c_add:
                return c_add
            if boxe.closest in c_add:
                c_add.add(boxe)
                return c_add
            if boxe in c_add:
                c_add.add(boxe.closest)
                return c_add
        new_c = Circuit()
        new_c.add(boxe)
        new_c.add(boxe.closest)
        return new_c


for boxe_pos in open('prod.txt'):
    x, y, z = boxe_pos.strip().split(',')
    Boxe(int(x), int(y), int(z))
# boxe_by_closest = {boxe.find_closest(): boxe for boxe in Boxe.all}
boxe_by_closest = sorted([(boxe.find_closest(), boxe) for boxe in Boxe.all])
print(boxe_by_closest)
for i, ( _, boxe) in enumerate(boxe_by_closest, start=1):
    print(boxe, boxe.closest)
    Circuit.join_or_create(boxe)
    # if i == 10:
    #     break

top_circuit = sorted(Circuit.all, reverse=True)
print(len(top_circuit[0]), len(top_circuit[1]), len(top_circuit[2]))
print(len(top_circuit[0]) * len(top_circuit[1]) * len(top_circuit[2]))
