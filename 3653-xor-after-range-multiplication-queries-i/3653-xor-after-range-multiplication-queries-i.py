class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        ans = 0
        
        MOD = 10**9+7

        for l,r,k,v in queries:
            for i in range(l,r+1,k):
                nums[i] = nums[i]*v%MOD

        for n in nums:
            ans ^= n

        return ans