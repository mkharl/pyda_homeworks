lst = map(int, input().split())
cnts = {}

for l in lst:
    if l not in cnts:
        cnts[l] = 1
    else:
        cnts[l] += 1

print(*sorted([k for k, v in cnts.items() if v > 1]))
