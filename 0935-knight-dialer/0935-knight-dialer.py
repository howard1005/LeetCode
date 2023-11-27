class Solution:
    def knightDialer(self, n: int) -> int:
        
        MOD = 1000000007
        
        d = {
            0:[4,6],
            1:[6,8],
            2:[7,9],
            3:[4,8],
            4:[3,9,0],
            5:[],
            6:[1,7,0],
            7:[2,6],
            8:[1,3],
            9:[2,4]
        }
        
        dp = [[0 for _ in range(10)] for _ in range(n)]
        for j in range(10):
            dp[-1][j] = 1
            
        for i in range(n-2,-1,-1):
            for j in range(10):
                for k in d[j]:
                    dp[i][j] += dp[i+1][k]
                dp[i][j] %= MOD
        
        return sum(dp[0])%MOD