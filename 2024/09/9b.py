class Block:
    def __init__(self, id_: int, lenght: int):
        self.id = id_
        self.lenght = lenght

    def __len__(self):
        return self.lenght

    def __bool__(self):
        return self.id != -1
    
    def __ge__(self, other):
        if isinstance(other, Block):
            return len(self) >= len(other)


class DiskFragmenter:

    def __init__(self):
        self.disk_map: str = open('9.txt').read()
        self.disk_repr: list[Block] = []
        for map_i, block_len in enumerate(self.disk_map):
            block_len = int(block_len)
            if map_i % 2:
                self.disk_repr.append(Block(-1, block_len))
            elif not map_i % 2:
                self.disk_repr.append(Block(map_i // 2, block_len))

    def defragment(self):
        for block in reversed(self.disk_repr):
            if not block:
                continue
            for free in self.disk_repr:
                if free is block:
                    break
                if free:
                    continue
                if free >= block:
                    i_b, i_f = self.disk_repr.index(block), self.disk_repr.index(free)
                    self.disk_repr[i_b - 1].lenght += len(block)
                    self.disk_repr.remove(block)
                    self.disk_repr.insert(i_f, block)
                    free.lenght -= len(block)
                    break

    @property
    def checksum(self) -> int:
        sum_ = 0
        i = 0
        for block in self.disk_repr:
            for _ in range(len(block)):
                if block:
                    sum_ += i * int(block.id)
                i += 1
        return sum_


disk_fragmenter = DiskFragmenter()
disk_fragmenter.defragment()
checksum = disk_fragmenter.checksum
print(disk_fragmenter.checksum)
