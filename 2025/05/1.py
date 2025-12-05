ranges, ids = open('prod.txt').read().split('\n\n')
ids = {int(i) for i in ids.split('\n')}
ranges = {i: (int(r1), int(r2)) for i, (r1, r2) in enumerate({tuple(r.split('-')) for r in ranges.split('\n')})}

fresh = set()
for r1, r2 in ranges.values():
    for i in ids:
        if r1 <= i <= r2:
            fresh.add(i)
print(len(fresh))


def optimise_ranges(bad_ranges: dict[int, tuple[int, int]]):
    opti_ranges = {}
    for r_id, (r1, r2) in bad_ranges.items():
        for o_id, (o1, o2) in opti_ranges.items():
            if r1 >= o1 and r2 <= o2:
                break
            if o1 <= r1 <= o2 <= r2:
                opti_ranges[o_id] = o1, r2
                break
            if r1 <= o1 <= r2 <= o2:
                opti_ranges[o_id] = r1, o2
                break
            if r1 <= o1 and r2 >= o2:
                opti_ranges[o_id] = r1, r2
                break
        else:
            opti_ranges[r_id] = r1, r2
    return opti_ranges


old_ranges = {}
while old_ranges != ranges:
    old_ranges = ranges.copy()
    ranges = optimise_ranges(old_ranges)
total = 0
for r1, r2 in ranges.values():
    total += r2 - r1 + 1
print(total)
