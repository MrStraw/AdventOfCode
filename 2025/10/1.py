from functools import reduce
from itertools import product, count
from operator import xor


class Machine:
    def __init__(self, leds_conditions: str, butons: list[str]):
        leds_schema = leds_conditions.strip('[]')
        self.condition: int = int(leds_schema.replace('.', '0').replace('#', '1'), 2)
        self.butons: tuple[int, ...] = tuple(
            int(''.join(str(int(i in {
                int(led_pos)
                for led_pos in buton_schema.strip('()').split(',')})) for i in range(len(leds_schema))), 2)
            for buton_schema in butons
        )

    def find_quikest(self) -> int:
        for i in count(1):
            for butons_order in product(self.butons, repeat=i):
                if self.condition == reduce(xor, butons_order):
                    return len(butons_order)


total = 0
for machine_schema in open('prod.txt'):
    leds_conditions, *butons, _ = machine_schema.strip().split(' ')
    total += Machine(leds_conditions, butons).find_quikest()
print(total)
