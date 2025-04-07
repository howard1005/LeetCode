class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot&1:
            return False
        target = tot//2
        
        dp = [[-1 for _ in range(100*len(nums))] for _ in range(len(nums))]
        def dfs(i,n):
            if i == len(nums):
                if n == 0:
                    return 1
                else:
                    return 0
            if dp[i][n] != -1:
                return dp[i][n]
            dp[i][n] = 0
            
            dp[i][n] |= dfs(i+1,n)
            if dp[i][n] == 0:
                dp[i][n] |= dfs(i+1,n-nums[i])
            return dp[i][n]
        return dfs(0,target)
            
        