import re


class LookAndSay:
    def __init__(self, seed: int):
        self.seed: str = str(seed)
        self.say = self.seed

    def grow(self, loops: int = 1):
        for _ in range(loops):
            looks = (match.group(0) for match in re.finditer(r'(.)\1*', self.say))
            self.say = ''.join(str(len(look)) + look[0] for look in looks)

las = LookAndSay(1113222113)
las.grow(50)
print(len(las.say))
