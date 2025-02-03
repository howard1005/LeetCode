class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 0

        def isIncreasing(l):
            for i in range(len(l)-1):
                if l[i] >= l[i+1]:
                    return False
            return True

        def isDecreasing(l):
            for i in range(len(l)-1):
                if l[i] <= l[i+1]:
                    return False
            return True

        def valid(l):
            return isIncreasing(l) or isDecreasing(l)

        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                l = nums[i:j]
                if valid(l):
                    ans = max(ans,len(l))
        
        return ans
                