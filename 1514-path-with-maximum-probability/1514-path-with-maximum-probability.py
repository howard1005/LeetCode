from heapq import heappush,heappop

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        d = defaultdict(list)
        for (a,b),p in zip(edges,succProb):
            d[a].append((b,p))
            d[b].append((a,p))
        
        vis = defaultdict(int)
        vis[start] = 1
        hq = [start]
        while hq:
            cur = heappop(hq)
            p = vis[cur]
            for ncur,np in d[cur]:
                if vis[ncur] < p*np:
                    vis[ncur] = p*np
                    heappush(hq, ncur)
        
        return vis[end]