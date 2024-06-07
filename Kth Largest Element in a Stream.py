import heapq


class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]

new = KthLargest(3, [4, 5, 8, 2])
print(new.add(3))
print(new.add(5))
print(new.add(10))
print(new.add(9))
print(new.add(4))
