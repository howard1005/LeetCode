from heapq import heappush,heappop

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:

        n = len(online)

        mn,mx = inf,-inf
        ed = defaultdict(list)
        for a,b,c in edges:
            if online[a] and online[b]:
                ed[a].append((b,c))
                mn,mx = min(mn,c),max(mx,c)


        def valid(m):
            vis = defaultdict(lambda:inf)
            vis[0] = 0
            hq = [(0,0)]
            while hq:
                c,i = heappop(hq)
                if vis[i] != c:
                    continue
                if i == n-1:
                    return True
                for ni,ec in ed[i]:
                    nc = c+ec
                    if ec<m or vis[ni]<=nc or k<nc:
                        continue
                    vis[ni] = nc
                    heappush(hq,(nc,ni))

            return False
            

        ans = -1
        
        lo,hi = mn,mx
        while lo<=hi:
            mi = (lo+hi)//2
            v = valid(mi)
            if v:
                lo = mi+1
                ans = max(ans,mi)
            else:
                hi = mi-1
        
        return ans