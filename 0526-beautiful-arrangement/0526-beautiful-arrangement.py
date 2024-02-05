class Solution:
    def countArrangement(self, n: int) -> int:
        d = defaultdict(set)
        
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i%j == 0 or j%i == 0:
                    d[i].add(j)
                    d[j].add(i)             
        
        dp = [-1 for _ in range((1<<n)+1)]
        
        def dfs(i,sta):
            if i == n+1:
                return 1
            
            if dp[sta] != -1:
                return dp[sta]
            dp[sta] = 0
            
            for j in range(n):
                if sta&(1<<j) == 0:
                    if j+1 in d[i]:
                        dp[sta] += dfs(i+1,sta|(1<<j))
            
            return dp[sta]
        
        ans = dfs(1,0)
        
        return ans
            
            
            