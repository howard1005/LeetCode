class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        
        p = inf
        
        for i in range(len(nums)-1,-1,-1):
            n = nums[i]
            if n > p:
                k = n//p+(1 if n%p else 0)
                ans += k-1
                p = n//k
            else:
                p = n
                
        return ans
            