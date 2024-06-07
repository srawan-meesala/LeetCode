import itertools
import operator 

class Solution:
    def largestAltitude(self, gain) -> int:
        return max(0, max(itertools.accumulate(gain, operator.add)))