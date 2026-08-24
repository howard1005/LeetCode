class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        
        cuml = [0 for _ in range(len(stones))]
        cuml[0] = stones[0]

        for i in range(1,len(cuml)):
            cuml[i] = stones[i]+cuml[i-1]


        dp = [0 for _ in range(len(stones))]
        dp[-1] = cuml[-1]

        
        for i in range(len(dp)-2,-1,-1):
            dp[i] = max(dp[i+1],cuml[i]-dp[i+1])

        ans = dp[1]

        return ans
        