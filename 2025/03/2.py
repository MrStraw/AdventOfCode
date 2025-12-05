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


def solve(source, digits, result=''):
    if len(result) == digits:
        return result
    chunk = source[:len(source) - (digits - len(result)) + 1]
    max_char = max(chunk)
    return int(solve(source[chunk.find(max_char) + 1:], digits, result + max_char))

# print(sum(largest_bank_joltage_2(bank_.strip()) for bank_ in open('prod.txt')))
print(sum(solve(bank_.strip(), 12) for bank_ in open('prod.txt')))
