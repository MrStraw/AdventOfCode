from itertools import batched

Tup_int = tuple[int, int]


class Arcade:

    def __init__(self, button_a: Tup_int, button_b: Tup_int, price: Tup_int):
        self.a = button_a
        self.b = button_b
        self.p = price

    @property
    def number_inputs(self) -> Tup_int | None:
        _ = self
        b = (_.p[1] * _.a[0] - _.p[0] * _.a[1]) / (_.b[1] * _.a[0] - _.b[0] * _.a[1])
        a = (_.p[0] - b * _.b[0]) / _.a[0]
        if all((a.is_integer(), b.is_integer())):
            return int(a), int(b)
        return None


tokens = 0
with open('13.txt') as f:
    for arcade_parms in batched(f, 4):
        _ = arcade_parms[0].split()
        a_params = int(_[2][2:-1]), int(_[3][2:])
        _ = arcade_parms[1].split()
        b_params = int(_[2][2:-1]), int(_[3][2:])
        _ = arcade_parms[2].split()
        convertion = 10000000000000
        price_coord = int(_[1][2:-1]) + convertion, int(_[2][2:]) + convertion

        arcade = Arcade(a_params, b_params, price_coord)
        inputs_requires = arcade.number_inputs
        # if inputs_requires and all(input_ <= 100 for input_ in inputs_requires):
        if inputs_requires:
            tokens += inputs_requires[0] * 3 + inputs_requires[1]

print(tokens)
