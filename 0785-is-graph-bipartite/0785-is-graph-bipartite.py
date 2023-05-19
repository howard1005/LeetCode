from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [-1 for _ in range(len(graph))]
        def proc(i):
            dq = deque()
            colors[i] = 0
            dq.append(i)
            while dq:
                v = dq.popleft()
                for nv in graph[v]:
                    if colors[nv] == -1:
                        colors[nv] = (colors[v]^1)
                        dq.append(nv)
                    elif colors[v] == colors[nv]:
                        return False
            return True
        l = [i for i in range(len(graph)-1,-1,-1)]
        while l:
            if not proc(l[-1]):
                return False
            while l and colors[l[-1]] != -1:
                l.pop()
        return True