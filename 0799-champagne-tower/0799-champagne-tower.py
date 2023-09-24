class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0 for _ in range(101)] for _ in range(101)]
        i = 0
        dp[0][0] = poured
        while i<100:
            for j in range(i+1):
                if dp[i][j] > 1:
                    n = dp[i][j] -1
                    dp[i][j] = 1
                    dp[i+1][j] += n/2
                    dp[i+1][j+1] += n/2
            i+=1
        return min(dp[query_row][query_glass],1)
            