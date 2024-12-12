class DiskFragmenter:

    def __init__(self):
        self.disk_map: str = open('9.txt').read()
        self.disk_repr = []
        for map_i, block_len in enumerate(self.disk_map):
            for block_i in range(int(block_len)):
                if map_i % 2:
                    self.disk_repr.append('.')
                else:
                    self.disk_repr.append(map_i // 2)

    def compact_fragment_the_disk(self):
        step = 0
        while '.' in self.disk_repr:
            end = self.disk_repr.pop()
            if end == '.':
                continue
            step = self.disk_repr.index('.', step)
            self.disk_repr[step] = end

    @property
    def checksum(self):
        sum_ = 0
        for i, id_ in enumerate(self.disk_repr):
            sum_ += i * id_
        return sum_


disk_fragmenter = DiskFragmenter()
disk_fragmenter.compact_fragment_the_disk()
print(disk_fragmenter.checksum)
