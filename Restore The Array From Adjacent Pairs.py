from collections import deque

adjacentPairs = [[4,-2],[1,4],[-3,1]]
dq = deque(adjacentPairs[0])
left,right = dq[0],dq[1]
for i in range(1, len(adjacentPairs)):
    k = adjacentPairs[i]
    if left in k:
        k.remove(left)
        dq.appendleft(k[0])
        left = dq[0]
    elif right in k:
        k.remove(right)
        dq.append(k[0])
        right = dq[-1]
print(list(dq))