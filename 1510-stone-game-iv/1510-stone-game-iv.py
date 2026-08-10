class Solution:
    dp = [[-1 for _ in range(100001)] for _ in range(2)] # 0:A 1:B
    def winnerSquareGame(self, n: int) -> bool:
        if self.dp[0][0] == -1:
            self.dp[0][0] = 0
            self.dp[1][0] = 1
            for i in range(1,100001):
                j = 1
                self.dp[0][i] = 0
                self.dp[1][i] = 1
                while i >= j*j and (self.dp[0][i]==0 or self.dp[1][i]==1):
                    self.dp[0][i] |= self.dp[1][i-j*j]
                    self.dp[1][i] &= self.dp[0][i-j*j]
                    j += 1
        

        ans = self.dp[0][n] == 1
        
        return ans
            