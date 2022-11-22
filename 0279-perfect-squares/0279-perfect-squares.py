class Solution:
    dp = [float('inf') for _ in range(10000+1)]
    def numSquares(self, n: int) -> int:
        #dp = [float('inf') for _ in range(n+1)]
        def dfs(num):
            if num == 0:
                return 0
            if self.dp[num] != float('inf'):
                return self.dp[num]
            i = 1
            while i*i <= num:
                self.dp[num] = min(self.dp[num],1+dfs(num-i*i))
                i += 1
            return self.dp[num]
        
        return dfs(n)