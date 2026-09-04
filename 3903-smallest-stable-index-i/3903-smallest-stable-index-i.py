class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i,n in enumerate(nums):
            if k >= max(nums[:i+1])-min(nums[i:]):
                return i
        return -1