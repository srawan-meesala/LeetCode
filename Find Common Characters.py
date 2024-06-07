from collections import Counter
def solve(words):
    d = dict(Counter(words[0]))
    for w in range(1, len(words)):
        for i in d:
            d[i] = min(d[i], words[w].count(i))
    res = []
    print(d)
    for i in d:
        for _ in range(d[i]):
            res.append(i)
    return res

words = ["bella","label","roller"]
print(solve(words))