from itertools import combinations


def largest_bank_joltage(bank: str) -> int:
    return max(int(''.join(c)) for c in combinations(bank, 2))



print(sum(largest_bank_joltage(bank_.strip()) for bank_ in open('prod.txt')))


