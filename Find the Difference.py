from collections import Counter
s = "a"
t = "aa"
def solve(s, t):
    c = Counter(s)
    for i in t:
        if i in c and c[i] > 0:
            c[i] -= 1
        else:
            return i
    for i, j in c.items():
        if j == 1:
            return i
print(solve(s, t))