def largest_bank_joltage_2(bank: str) -> int:
    selected = ''
    while len(selected) < 12:
        for d in '987654321':
            if d not in bank:
                continue
            first_pos = bank.find(d)
            if len(selected) + len(bank[first_pos:]) < 12:
                continue
            selected += d
            bank = bank[first_pos + 1:]
            break

    return int(selected)
    

sum_joltage = 0
for i, bank_ in enumerate(open('prod.txt'), start=1):
    sum_joltage += largest_bank_joltage_2(bank_.strip())
print(sum_joltage)
