class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        stones = piles
        dp = [[-1 for _ in range(len(stones))] for _ in range(len(stones))]
        
        def dfs(l,r,n,flag): # allice flag=1, bob flag=-1
            if l==r:
                return 0
            if dp[l][r] != -1:
                return dp[l][r]
            if flag == 1:
                val = 0
                val = max(val,dfs(l+1,r,n-stones[l],-flag) + flag*(n-stones[l]))
                val = max(val,dfs(l,r-1,n-stones[r],-flag) + flag*(n-stones[r]))
                dp[l][r] = val
            else:
                val = 1000000000
                val = min(val,dfs(l+1,r,n-stones[l],-flag) + flag*(n-stones[l]))
                val = min(val,dfs(l,r-1,n-stones[r],-flag) + flag*(n-stones[r]))
                dp[l][r] = val
            return dp[l][r]
        
        dfs(0,len(stones)-1,sum(stones),1)
        
        print(dp)
        
        return True