import heapq
stones = [10,4,2,10]
heapq._heapify_max(stones)
while len(stones) > 1:
    a = heapq.heappop(stones)
    b = heapq.heappop(stones)
    print(a, b)
    if a == b: pass
    elif a > b: heapq.heappush(stones, a - b)
    elif a < b: heapq.heappush(stones, b - a)
print(stones)