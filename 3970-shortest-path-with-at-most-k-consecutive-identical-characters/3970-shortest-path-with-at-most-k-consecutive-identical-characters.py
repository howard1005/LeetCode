from heapq import heappush,heappop

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        ans = inf

        ed = defaultdict(list)
        for a,b,c in edges:
            ed[a].append((b,c))
        
        vis = defaultdict(lambda:inf) # (i,cnt):cost

        vis[(0,1)] = 0
        hq = [(0,0,1)] # cost,idx,cnt

        while hq:
            cost,i,cnt = heappop(hq)
            if vis[(i,cnt)] != cost:
                continue
            for ni,c in ed[i]:
                ncost = c+cost
                ncnt = 1
                if labels[i] == labels[ni]:
                    ncnt = cnt+1
                if ncnt > k:
                    continue
                if vis[(ni,ncnt)] <= ncost:
                    continue
                vis[(ni,ncnt)] = ncost
                heappush(hq,(ncost,ni,ncnt))

        # print(vis)

        for j in range(k+1):
            ans = min(ans,vis[(n-1,j)])

        return ans if ans != inf else -1