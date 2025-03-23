from heapq import heappush,heappop

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 1000000007

        ed = defaultdict(list)

        for a,b,c in roads:
            ed[a].append((b,c))
            ed[b].append((a,c))

        visd = defaultdict(lambda:inf)
        cntd = defaultdict(int)

        visd[0] = 0
        cntd[0] = 1
        hq = [(0,0)]

        while hq:
            c,i = heappop(hq)
            if visd[i] != c:
                continue
            for ni,nc in ed[i]:
                if visd[ni] < nc+c:
                    pass
                elif visd[ni] == nc+c:
                    cntd[ni] += cntd[i]
                    cntd[ni] %= MOD
                else:
                    visd[ni] = nc+c
                    cntd[ni] = cntd[i]
                    heappush(hq,(nc+c,ni))

        return cntd[n-1]