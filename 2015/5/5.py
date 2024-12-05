import re

regex1 = r"(?=.*([aeiou].*){3,})(?=.*(.)\2)(?!.*(ab|cd|pq|xy))"
regex2 = r"(?=.*(..).*\1)(?=.*(.).\2)"

total1, total2 = 0, 0
with open('5.txt') as f:
    for line in f:
        total1 += bool(re.match(regex1, line.rstrip()))
        total2 += bool(re.match(regex2, line.rstrip()))

print(total1)
print(total2)
