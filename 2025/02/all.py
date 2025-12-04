def numbers():
    for whole_range in open('prod.txt').read().split(','):
        a, b = whole_range.split('-')
        yield from range(int(a), int(b) + 1)
        
def is_valid_1(number: int) -> bool:
    str_ = str(number)
    len_ = len(str_)
    return True if len_ % 2 else str_[:len_//2] != str_[len_//2:]

def is_valid_2(number: int) -> bool:
    str_ = str(number)
    len_ = len(str_)
    for i in range(1, len_ // 2 + 1):
        if len_ % i == 0 and str_ == len_ // i * str_[:i]:
            return False
    return True


no_valids = 0
for n in numbers():
    if not is_valid_2(n):
        no_valids += n
print(no_valids)