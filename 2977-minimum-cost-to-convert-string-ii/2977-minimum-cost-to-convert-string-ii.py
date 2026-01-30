from heapq import heappush,heappop

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        ans = inf

        trd = set()
        for o in original:
           s = ''
           for c in o:
               s += c
               trd.add(s) 
        
        l = list(set(original+changed))
        # print(l)
        rid = {}
        for i,s in enumerate(l):
            rid[s] = i
        ed = defaultdict(set)
        for org,ch,c in zip(original,changed,cost):
            ed[rid[org]].add((rid[ch],c))
        
        d = {}
        def dis(si):
            vis = defaultdict(lambda:inf)
            vis[si] = 0
            hq = [(0,si)]
            while hq:
                c,i = heappop(hq)
                if c > vis[i]:
                    continue
                for ni,nc in ed[i]:
                    if c+nc < vis[ni]:
                        vis[ni] = c+nc
                        heappush(hq,(c+nc,ni))
            for j,c in vis.items():
                d[(si,j)] = c
        for i in range(len(l)):
            dis(i)

        # print(d)

        
        @cache
        def dfs(i):
            if i == len(source):
                return 0
            ret = inf
            os = ''
            cs = ''
            for j in range(i,len(source)):
                os += source[j]
                cs += target[j]
                if os not in trd:
                    break
                if os == cs:
                    ret = min(ret, dfs(j+1))
                elif os in rid and cs in rid:
                    oi = rid[os]
                    ci = rid[cs]
                    if (oi,ci) in d:
                        mnc = d[(oi,ci)]
                        ret = min(ret, mnc+dfs(j+1))
            # print('dfs',i,ret)
            return ret

        ans = dfs(0)

        return ans if ans != inf else -1
