from pathlib import Path
from typing import Iterator


def instructions() -> Iterator[tuple[str, int]]:
    file = Path(__file__).parent / 'file.txt'
    with file.open() as f:
        for line in f:
            line = line.strip()
            yield line[0], int(line[1:])


def rotate(start: int, direction: str, value: int) -> int:
    return (start + (-value if direction == 'L' else value)) % 100

step, i = 50, 0
for d, r in instructions():
    step = rotate(step, d, r)
    if step == 0:
        i += 1

print(i)
