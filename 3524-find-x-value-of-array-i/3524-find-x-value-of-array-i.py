class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0 for _ in range(k)]

        dp = [[0 for _ in range(k)] for _ in range(len(nums))]

        dp[0][nums[0]%k] = 1

        for i in range(1,len(nums)):
            r = nums[i]%k
            dp[i][r] += 1
            for j in range(k):
                dp[i][j*r%k] += dp[i-1][j]

        # print(dp)
                
        for i in range(len(nums)):
            for j in range(k):
                ans[j] += dp[i][j]
        

        return ans