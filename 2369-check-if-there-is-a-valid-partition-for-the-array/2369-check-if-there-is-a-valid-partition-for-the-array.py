class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [False for _ in range(len(nums)+1)]
        dp[-1] = True
        
        for i in range(len(nums)-1,-1,-1):
            if i+1 < len(nums):
                if nums[i] == nums[i+1]:
                    dp[i] |= dp[i+2]
            if i+2 < len(nums):
                if nums[i] == nums[i+1] and nums[i+1] == nums[i+2]:
                    dp[i] |= dp[i+3]
                if nums[i]+1 == nums[i+1] and nums[i+1]+1 == nums[i+2]:
                    dp[i] |= dp[i+3]
        
        return dp[0]
                    