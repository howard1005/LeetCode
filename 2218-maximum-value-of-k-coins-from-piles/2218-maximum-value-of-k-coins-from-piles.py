class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [[0 for _ in range(k+1)] for _ in range(len(piles))]
        
        l = [len(p) for p in piles]
        for i in range(len(l)-2,-1,-1):
            l[i] += l[i+1]
            
        ll = [[0] for p in piles]
        for i in range(len(ll)):
            tl = ll[i]
            for a in piles[i]:
                tl.append(tl[-1]+a)
        
        cum = 0
        for j in range(k+1):
            dp[-1][j] = cum
            if j < len(piles[-1]):
                cum += piles[-1][j]
        
        for i in range(len(piles)-2,-1,-1):
            for j in range(min(k+1, l[i]+1)):
                for a in range(max(0, j-l[i+1]), min(j+1, len(ll[i]))):
                    dp[i][j] = max(dp[i][j], ll[i][a] + dp[i+1][j-a])
                        

        return dp[0][k]