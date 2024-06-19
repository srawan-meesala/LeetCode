import heapq
def solve(k, w, profits, capital):
    projects = [[capital[i], profits[i]] for i in range(len(capital))]
    projects.sort()
    if w < projects[0][0]: return 0

    heap = []
    n = len(capital)
    i = 0

    for _ in range(min(k, n)):
        while i<n and projects[i][0]<=w:
            heapq.heappush(heap, projects[i][1])
            i += 1
        print(heap)
        if not heap: break
        w += heapq.heappop(heap)

    return w

k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]
print(solve(k, w, profits, capital))