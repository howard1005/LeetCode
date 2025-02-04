class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = 0

        def vaild(l):
            for i in range(len(l)-1):
                if l[i] >= l[i+1]:
                    return False
            return True

        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                l = nums[i:j]
                if vaild(l):
                    ans = max(ans,sum(l))
        
        return ans
                