from bisect import bisect_right

R, I = open('prod.txt').read().split('\n\n')

R, curr = sorted(tuple(map(int, f.split('-'))) for f in R.split()), -1
scan = [curr := max(curr, x) for x in (val for r1, r2 in R for val in (r1, r2 + 1))]

print(sum(bisect_right(scan, i) % 2 for i in {*map(int, I.split())}))
print(sum(scan[1::2]) - sum(scan[::2]))
