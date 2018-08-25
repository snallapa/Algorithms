#leetcode 39
candidates = [2,3,6,7]
target = 7
possibilities = [[[]] for n in range(target+1)]
for i in range(1, target+1):
    currentPoss = set([])
    for candidate in candidates:
        if i - candidate < 0:
            continue
        for poss in possibilities[i - candidate]:
            currentPoss.add(tuple(sorted(list(poss) + [candidate])))
    possibilities[i] = list(currentPoss)
print(possibilities)
