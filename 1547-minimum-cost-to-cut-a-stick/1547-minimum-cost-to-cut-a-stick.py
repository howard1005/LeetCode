from bisect import bisect_left

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]
        dp = [[0 for _ in range(len(cuts))] for _ in range(len(cuts))]
        
        for size in range(3,len(cuts)+1):
            for i in range(len(cuts)-size+1):
                j = i+size-1
                mn = inf
                for k in range(i+1,j):
                    mn = min(mn,(cuts[j]-cuts[i]) + dp[i][k] + dp[k][j])                    
                dp[i][j] = mn
                
        return dp[0][-1]