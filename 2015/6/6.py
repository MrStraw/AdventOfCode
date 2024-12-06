class LightGrid:
    def __init__(self):
        self.matrice: list[list[int]] = [[0 for x in range(1000)] for y in range(1000)]

    def command(self, do: str, c1: str, c2: str):
        c1x, c1y = c1.split(',')
        c2x, c2y = c2.split(',')
        for x in range(int(c1x), int(c2x) + 1):
            for y in range(int(c1y), int(c2y) + 1):
                match do:
                    case 'toggle':
                        self.matrice[y][x] += 2
                    case 'on':
                        self.matrice[y][x] += 1
                    case 'off':
                        if self.matrice[y][x]:
                            self.matrice[y][x] -= 1


lights = LightGrid()

with open('6.txt') as f:
    for line in f:
        match line.split():
            case ['turn', instruction, _c1, 'through', _c2]:
                lights.command(instruction, _c1, _c2)
            case ['toggle', _c1, 'through', _c2]:
                lights.command('toggle', _c1, _c2)

ons = 0
for row in lights.matrice:
    for light in row:
        ons += light
print(ons)
