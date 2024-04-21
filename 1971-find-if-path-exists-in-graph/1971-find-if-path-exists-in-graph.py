from collections import deque,defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        ev = defaultdict(list)
        dq = deque()
        for s,e in edges:
            ev[s].append(e)
            ev[e].append(s)
        vis = {source:1}
        dq.append(source)
        while dq:
            a = dq.popleft()
            if a == destination:
                return True
            for b in ev[a]:
                if b not in vis:
                    vis[b] = 1
                    dq.append(b)

        return False