lst = map(int, input().split())
cnts = {}

for l in lst:
    cnts.setdefault(l, 0)
    cnts[l] += 1

print(*sorted([k for k, v in cnts.items() if v > 1]))
