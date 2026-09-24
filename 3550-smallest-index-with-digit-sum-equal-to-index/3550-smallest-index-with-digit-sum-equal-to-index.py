class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i,n in enumerate(nums):
            if sum([int(c) for c in str(n)]) == i:
                return i
        return -1