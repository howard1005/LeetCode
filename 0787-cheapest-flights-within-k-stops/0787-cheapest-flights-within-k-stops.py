from heapq import heappush,heappop

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        ans = inf
        
        edges = [[] for _ in range(n)]
        for f,t,p in flights:
            edges[f].append((t,p))
        
        ps = [[inf for _ in range(k+2)] for _ in range(n)]
        
        ps[0][0] = 0
        hq = [(0,src,0)] # cost,idx,k
        while hq:
            c,i,kk = heappop(hq)
            # print(c,i,kk,ps[i][kk])
            if c > ps[i][kk]:
                continue
            if i == dst:
                ans = min(ans,c)
            if kk > k:
                continue
            for t,p in edges[i]:
                if ps[t][kk+1] > c+p:
                    ps[t][kk+1] = c+p
                    heappush(hq,(c+p,t,kk+1))
        
        return -1 if ans == inf else ans