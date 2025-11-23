class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        ans = 0

        dp = [[-1 for _ in range(3)] for _ in range(len(nums))]
        for j in range(3):
            n = nums[-1]
            m = (n+j)%3
            if m == 0:
                dp[-1][j] = n
        
        for i in range(len(nums)-2,-1,-1):
            n = nums[i]
            for j in range(3):
                if dp[i+1][j] != -1:
                    dp[i][j] = max(dp[i][j],dp[i+1][j])
                m = (n+j)%3
                if m == 0:
                    dp[i][j] = max(dp[i][j],n)
                if dp[i+1][m] != -1:
                    dp[i][j] = max(dp[i][j],dp[i+1][m]+n)
                
        ans = dp[0][0]

        return ans if ans != -1 else 0
        