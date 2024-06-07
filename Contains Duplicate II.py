class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d.keys() and abs(i - d[nums[i]])<=k:
                return True
            d[nums[i]] = i
        return False