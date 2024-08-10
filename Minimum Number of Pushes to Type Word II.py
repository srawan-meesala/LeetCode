from collections import Counter

def solve(word):
    res = 0
    dis_elements = len(set(word))
    cnt = Counter(word)
    print(cnt)
    values = list(cnt.values())
    values.sort(reverse=True)
    for i in range(dis_elements):
        res += values[i]*((i//8) + 1)
    return res

print(solve("buqmhaluhtsalccbpxxgopeko"))