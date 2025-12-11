from itertools import product, count


ti = tuple[int, ...]

class Machine:
    def __init__(self, power_need: str, butons: list[str]):
        self.power_need: ti = tuple(int(i) for i in power_need.strip('{}').split(','))
        self.butons: tuple[ti, ...] = tuple(tuple(
            int(i in {int(led_pos) for led_pos in buton_schema.strip('()').split(',')})
            for i in range(len(self.power_need))) for buton_schema in butons)
        self.histo: dict[str, ti] = {}
        self._power_range: range = range(len(self.power_need))

    def press(self, buton_pos: int, from_power: ti) -> tuple[ti, ti]:
        after = tuple(p + self.butons[buton_pos][i] for i, p in enumerate(from_power))
        

    def iter_press(self, butons_pos: ti) -> ti:
        buton_pos_str = '.'.join(str(b) for b in butons_pos)
        if buton_pos_str not in self.histo:
            # if self.histo[butons_pos] is None
            if len(butons_pos) > 1:
                *before, plus = butons_pos
                pressed = self.press(plus, self.histo['.'.join(str(b) for b in before)])
                too_far = any(self.power_need[i] - pressed[i] < 1 for i in self._power_range)
                self.histo[buton_pos_str] = None if too_far else pressed
            else:
                self.histo[buton_pos_str] = self.butons[butons_pos[0]]
        return self.histo[buton_pos_str]

    def find_quikest(self):
        all_butons_pos = tuple(_ for _ in range(len(self.butons)))
        for i in count():
            if i == 0:
                continue
            for buttons_order in product(all_butons_pos, repeat=i):
                if self.iter_press(buttons_order) == self.power_need:
                    return buttons_order


total = 0
for machine_schema in open('dev.txt'):
    _, *butons, powers_need = machine_schema.strip().split(' ')
    m = Machine(powers_need, butons)
    print(m.__dict__)
    print(m.find_quikest())
    break
print(total)
