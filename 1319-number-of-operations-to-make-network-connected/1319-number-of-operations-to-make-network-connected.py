class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        d = defaultdict(list)
        
        for a,b in connections:
            d[a].append(b)
            d[b].append(a)
        
        spare = 0
        need = -1
        vis = {}
        
        def bfs(si):
            nonlocal spare
            vis[si] = 1
            dq = deque([si])
            while dq:
                i = dq.popleft()
                for ni in d[i]:
                    if ni not in vis:
                        vis[ni] = 1
                        spare -= 1
                        dq.append(ni)
                    else:
                        spare += 1
        
        for i in range(n):
            if i not in vis:
                # print(i)
                bfs(i)
                need += 1
        
        # print(spare,need)
        spare //= 2
        if need > spare:
            return -1
        return need
        
        
        