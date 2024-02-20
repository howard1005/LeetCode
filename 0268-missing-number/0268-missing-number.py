class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = 1
        for i in range(len(nums)+1):
            if i not in d:
                return i
        return -1