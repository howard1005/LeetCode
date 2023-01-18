class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        ans = 0
        
        dp = [[n,1] for n in nums]
        ans = dp[0][0]
        for i in range(1,len(nums)):
            if dp[i-1][0]+dp[i][0] > dp[i][0]:
                dp[i][0] += dp[i-1][0]
                dp[i][1] += dp[i-1][1]
            ans = max(ans,dp[i][0])
            
        dp = [[n,1] for n in nums]
        for i in range(1,len(nums)):
            if dp[i-1][0]+dp[i][0] < dp[i][0]:
                dp[i][0] += dp[i-1][0]
                dp[i][1] += dp[i-1][1]
        cum = sum(nums)
        for mn,size in dp:
            if cum-mn > ans and size != len(nums):
                ans = cum-mn
                
        return ans