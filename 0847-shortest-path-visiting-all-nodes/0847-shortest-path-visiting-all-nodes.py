from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        dp = [[float('inf') for _ in range(1<<n)] for _ in range(n)]

        def proc(s):
            dq = deque()
            for i,sta in s:
                dq.append((i,sta))
            #print(dq)
            while dq:
                i,sta = dq.popleft()
                for j in graph[i]:
                    if sta|(1<<j) and dp[j][sta]>dp[i][sta]+1:
                        dp[j][sta] = dp[i][sta]+1
                        s.add((j,sta))
                        dq.append((j,sta))
            ret = set()
            for i,sta in s:
                for j in graph[i]:
                    nsta = sta^(1<<i)
                    if nsta&(1<<j) and dp[j][nsta]>dp[i][sta]+1:
                        dp[j][nsta] = dp[i][sta]+1
                        ret.add((j,nsta))
            return ret
                    
        s = set()
        for i in range(n):
            dp[i][(1<<n)-1] = 0
            s.add((i,(1<<n)-1))
        for i in range(n+1):
            s = proc(s)
        #print(dp)
            
        ans = float('inf')
        for i in range(n):
            ans = min(ans,dp[i][1<<i])
        return ans