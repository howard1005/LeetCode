from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ld = [defaultdict(list) for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                ld[i][nums[j]].append(j)
        
        dp = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]
        def dfs(i,j):
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = 0
            ret = 0
            diff = nums[j]-nums[i]
            for k in ld[j][nums[j]+diff]:
                ret += dfs(j,k) + 1
            dp[i][j] = ret
            return ret
        
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                ans += dfs(i,j)
                
        
        return ans
            