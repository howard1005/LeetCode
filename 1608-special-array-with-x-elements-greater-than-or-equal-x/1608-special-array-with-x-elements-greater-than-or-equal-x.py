from bisect import bisect_left

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for x in range(1000):
            i = bisect_left(nums,x)
            if x == len(nums)-i:
                return x
        return -1
            