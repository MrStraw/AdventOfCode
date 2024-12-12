rules: list[tuple[int, int]] = []
to_orders: list[list[int]] = []

with open('5.txt') as f:
    rules_to_updates = False
    for line in f:
        line = line.rstrip()

        if not line:
            rules_to_updates = True
            continue

        if not rules_to_updates:
            str_tuple = line.split('|')
            rules.append((int(str_tuple[0]), int(str_tuple[1])))
        else:
            to_orders.append([int(page) for page in line.split(',')])


def order_pages_rules():
    after_rules: dict[int, set[int]] = {}

    for rule in rules:
        before, after = rule
        if after not in after_rules:
            after_rules[after] = set()
        after_rules[after].add(before)

    return after_rules


rules_order = order_pages_rules()



def orderator(to_order: list[int]) -> list[int]:
    clean_rules_order = {}
    for page in to_order:
        clean_rules_order[page] = {p for p in rules_order[page] if p in to_order}

    len_rules_order = {}
    for page, pages in clean_rules_order.items():
        len_rules_order[len(pages)] = page

    solution = []
    for order in sorted(len_rules_order):
        solution.append(len_rules_order[order])

    return solution


mid_addition = 0
# to_updates = [to_updates[0]]
for to_order in to_orders:
    ordered = orderator(to_order)
    assert set(ordered) == set(to_order)
    assert len(ordered) % 2 == 1
    if ordered != to_order:
        mid_addition += ordered[len(ordered) // 2]

print(mid_addition)
