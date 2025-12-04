from itertools import combinations


def largest_bank_joltage(bank: str) -> int:
    return max(int(''.join(c)) for c in combinations(bank, 2))



sum_joltage = 0
for i, bank_ in enumerate(open('prod.txt'), start=1):
    sum_joltage += largest_bank_joltage(bank_)

print(sum_joltage)


