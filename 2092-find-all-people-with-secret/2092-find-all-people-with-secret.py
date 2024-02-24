class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        kd = {0,firstPerson}
        td = defaultdict(list)

        def bfs(i,ed,vis):
            vis[i] = 1
            dq = deque([i])
            while dq:
                cur = dq.popleft()
                for ncur in ed[cur]:
                    if ncur in vis:
                        continue
                    vis[ncur] = 1
                    dq.append(ncur)
        
        for x,y,t in meetings:
            td[t].append((x,y))
            
        for t in sorted(td.keys()):
            vis = {}
            ed = defaultdict(list)
            keys = set()
            for x,y in td[t]:
                ed[x].append(y)
                ed[y].append(x)
                if x in kd:
                    keys.add(x)
                if y in kd:
                    keys.add(y)
            for k in keys:
                if k not in vis:
                    bfs(k,ed,vis)
            for k in vis:
                kd.add(k)
            
        return list(kd)
        
        
        