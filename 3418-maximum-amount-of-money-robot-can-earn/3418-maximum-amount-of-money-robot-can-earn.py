class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        ans = 0

        m,n = len(coins),len(coins[0])

        dp = [[[-inf for _ in range(3)] for _ in range(n)] for _ in range(m)]

        dp[0][0][2] = coins[0][0]
        dp[0][0][1] = 0

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                for k in range(3):
                    c = -inf
                    # print(i,j,k,c)
                    if i>0:
                        c = max(c,dp[i-1][j][k]+coins[i][j])
                        if k < 2:
                            c = max(c,dp[i-1][j][k+1])
                    if j>0:
                        c = max(c,dp[i][j-1][k]+coins[i][j])
                        if k < 2:
                            c = max(c,dp[i][j-1][k+1])
                    # print(i,j,k,c)
                    dp[i][j][k] = c

        # print("\ndp")
        # for r in dp:
        #     print(r)

        ans = max(dp[-1][-1])

        return ans