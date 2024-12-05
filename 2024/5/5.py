rules_order: dict[int, set[int]] = {}
to_orders: list[list[int]] = []

with open('5.txt') as f:
    rules_to_updates = False
    for line in f:
        line = line.rstrip()

        if not line:
            rules_to_updates = True
            continue

        if not rules_to_updates:
            before, after = int(line[:2]), int(line[3:])
            if after not in rules_order:
                rules_order[after] = set()
            rules_order[after].add(before)
        else:
            to_orders.append([int(page) for page in line.split(',')])


def orderator(to_order: list[int]) -> list[int]:
    len_rules_order = {len({p for p in rules_order[page] if p in to_order}): page for page in to_order}
    return [len_rules_order[order] for order in sorted(len_rules_order)]


mid_good, mid_bad = 0, 0
for to_order_ in to_orders:
    ordered = orderator(to_order_)
    mid = ordered[len(ordered) // 2]
    if ordered == to_order_:
        mid_good += mid
    else:
        mid_bad += mid

print("Good:", mid_good)
print("Bad:", mid_bad)
