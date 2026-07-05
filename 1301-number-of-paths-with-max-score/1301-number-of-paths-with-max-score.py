class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        ans = [0,0]
        
        MOD = 10**9+7

        n = len(board)

        dp = [[[0,0] for _ in range(n)] for _ in range(n)]
        dp[-1][-1] = [0,1]

        for i in range(n-2,-1,-1):
            c = board[i][-1]
            if c == 'X':
                continue
            v = int(c)
            if dp[i+1][-1][1]:
                dp[i][-1][0] += v+dp[i+1][-1][0]
                dp[i][-1][1] += dp[i+1][-1][1]

        for j in range(n-2,-1,-1):
            c = board[-1][j]
            if c == 'X':
                    continue
            v = int(c)
            if dp[-1][j+1][1]:
                dp[-1][j][0] += v+dp[-1][j+1][0]
                dp[-1][j][1] += dp[-1][j+1][1]

        for i in range(n-2,-1,-1):
            for j in range(n-2,-1,-1):
                c = board[i][j]
                if c == 'X':
                    continue
                v = int(c) if c.isdigit() else 0 
                mx = max(dp[i+1][j][0],dp[i+1][j+1][0],dp[i][j+1][0])
                if sum([dp[i+1][j][1],dp[i+1][j+1][1],dp[i][j+1][1]]) == 0:
                    continue
                dp[i][j][0] += v+mx
                if dp[i+1][j][0] == mx:
                    dp[i][j][1] += dp[i+1][j][1]
                if dp[i+1][j+1][0] == mx:
                    dp[i][j][1] += dp[i+1][j+1][1]
                if dp[i][j+1][0] == mx:
                    dp[i][j][1] += dp[i][j+1][1]
                dp[i][j][1] %= MOD

        # for r in dp:
        #     print(r)

        ans = dp[0][0]

        return ans