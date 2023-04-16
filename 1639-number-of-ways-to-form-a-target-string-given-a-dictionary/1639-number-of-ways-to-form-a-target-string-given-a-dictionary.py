from bisect import bisect_left
from collections import Counter

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        
        MOD = 1000000007
        
        d = defaultdict(list)
        
        for word in words:
            for i,c in enumerate(word):
                d[c].append(i)
                
        for c in d:
            d[c] = Counter(d[c])
            
        dp = [[0 for _ in range(len(words[0]))] for _ in range(len(target))]
        
        
        for j in range(len(words[0])-1,-1,-1):
            dd = d[target[-1]]
            cnt = dd[j] if j in dd else 0
            dp[-1][j] = cnt 
            if j+1 < len(words[0]):
                dp[-1][j] += dp[-1][j+1]
        
        for i in range(len(target)-2,-1,-1):
            dd = d[target[i]]
            for j in range(len(words[0])-2,-1,-1):
                cnt = dd[j] if j in dd else 0
                dp[i][j] = (dp[i][j+1] + cnt * dp[i+1][j+1]) % MOD
                
        return dp[0][0]
                