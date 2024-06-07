import heapq

k = 1
points = [[1,3],[-2,2]]

print(heapq.nsmallest(k, points, key=lambda i: (i[0]**2 + i[1]**2)))