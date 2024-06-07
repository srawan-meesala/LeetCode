from collections import Counter
import heapq
def solve(hand, groupSize):
    if len(hand) % groupSize != 0: return False
    heapq.heapify(hand)
    print(hand)
    while hand:
        start = heapq.heappop(hand)
        for i in range(groupSize):
            if start + i in hand:
                k = hand.remove(start+i)
                pass    
            else:
                return False
    return True

hand = [1,1,2,2,3,3]
groupSize = 2
print(solve(hand, groupSize))