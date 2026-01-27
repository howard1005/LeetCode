from heapq import heappush,heappop

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        ans = inf

        ed = defaultdict(set)
        for a,b,c in edges:
            ed[a].add((b,c))
            ed[b].add((a,2*c))

        vis = defaultdict(lambda:inf)
        vis[0] = 0
        hq = [(0,0)]
        while hq:
            c,i = heappop(hq)
            # print(c,i)
            if c != vis[i]:
                continue
            if i == n-1:
                ans = c
                break
            for ni,w in ed[i]:
                nc = c+w
                if vis[ni] > nc:
                    vis[ni] = min(vis[ni],nc)
                    heappush(hq,(nc,ni))

        return ans if ans != inf else -1