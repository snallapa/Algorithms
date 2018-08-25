#leetcode 22
n = 3
parens = [[""]] + [[] for i in range(n)]
def insert(s, ins, i):
    return s[:i] + ins + s[i:]
for i in range(1, n+1):
    prev = parens[i-1]
    newParens = set([])
    for paren in prev:
        for j in range(len(paren) + 1):
            newParens.add(insert(paren, "()", j))
    parens[i] = list(newParens)

print(parens)
