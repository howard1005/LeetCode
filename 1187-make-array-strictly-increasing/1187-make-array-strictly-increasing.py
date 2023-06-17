from bisect import bisect_right

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        arr = arr1+arr2
        cnt = 0
        d = {}
        for n in arr:
            if n not in d:
                d[n] = cnt
                cnt += 1
        
        dp = [[0 for _ in range(cnt)] for _ in range(len(arr1)+1)]
        
        for i in range(len(arr1)-1,-1,-1):
            for pn,k in d.items():
                if i == 0:
                    pn = -1
                n = arr1[i]
                nn = n
                jj = bisect_right(arr2,pn)
                if jj < len(arr2):
                    nn = arr2[jj]
                
                dp[i][k] = inf
                
                if pn < n:
                    dp[i][k] = min(dp[i][k],dp[i+1][d[n]])
                if pn < nn:
                    dp[i][k] = min(dp[i][k],dp[i+1][d[nn]]+1)
            
        if dp[0][0] == inf:
            return -1
        
        return dp[0][0]
                