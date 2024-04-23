from heapq import heappush,heappop

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        d = defaultdict(set)
        for a,b in edges:
            d[a].add(b)
            d[b].add(a)
            
        hs = [[] for _ in range(n)]
        def getMin(par,cur):
            if hs[cur] and hs[cur][0][1] != par:
                return hs[cur][0][0]
            if len(hs[cur]) >= 2:
                t = heappop(hs[cur])
                ret = hs[cur][0][0]
                heappush(hs[cur],t)
                return ret
            return 0
            
        def dfs(par,cur):
            sd = d[cur]
            for child in sd.copy():
                if child == par:
                    continue
                sd.remove(child)
                heappush(hs[cur],(-(dfs(cur,child)+1),child))
                
            return -getMin(par,cur)
        
        ansd = defaultdict(list) 
        for node in range(n):
            ans = dfs(-1,node)
            # print(node,ans)
            ansd[ans].append(node)
        mn = min(ansd.keys())
        return ansd[mn]
        
        
        
        return ansd[mn]