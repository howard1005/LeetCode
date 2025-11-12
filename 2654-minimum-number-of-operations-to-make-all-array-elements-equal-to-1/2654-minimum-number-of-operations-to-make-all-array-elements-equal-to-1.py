from math import gcd

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = nums.count(1)
        if cnt:
            return len(nums)-cnt

        ans = -1

        def proc(size):
            for i in range(len(nums)-size+1):
                if gcd(*nums[i:i+size]) == 1:
                    return True
        
        for size in range(2,len(nums)+1):
            if proc(size):
                ans = len(nums)+size-2
                break

        return ans