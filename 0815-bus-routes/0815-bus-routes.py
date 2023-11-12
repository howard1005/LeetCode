from heapq import heappush,heappop

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        d = defaultdict(list)
        for i,route in enumerate(routes):
            for j in range(len(route)):
                a,b = route[j],route[(j+1)%len(route)]
                d[a].append((b,i))
        
        
        vis = defaultdict(lambda:inf)
        hq = []
        vis[(-1,source)] = 0
        heappush(hq,(0,-1,source)) 
        while hq:
            c,b,n = heappop(hq) # cost,bus,node
            if c > vis[(b,n)]:
                continue
            if n == target:
                return c
            for nn,bb in d[n]:
                cc = c + (0 if bb == b else 1)
                if vis[(bb,nn)] > cc:
                    vis[(bb,nn)] = cc
                    heappush(hq,(cc,bb,nn))
        return -1