class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        ans = {j for j in range(n)}

        ed = defaultdict(set)

        for a,b in invocations:
            ed[a].add(b)

        dq = deque([k])
        vis = {k}
        while dq:
            i = dq.popleft()
            for j in ed[i]:
                if j in vis:
                    continue
                vis.add(j)
                dq.append(j)
        
        # print(vis)
        nvis = set()
        
        def bfs(i):
            nvis.add(i)
            dq.append(i)
            while dq:
                i = dq.popleft()
                for j in ed[i]:
                    if j in nvis:
                        continue
                    if j in vis:
                        return False
                    nvis.add(j)
                    dq.append(j)
            return True

        f = True
        for i in range(n):
            if i not in vis and i not in nvis:
                if not bfs(i):
                    f = False
                    break
        
        if f:
            ans -= vis 

        return list(ans)