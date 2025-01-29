from collections import deque
from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for edge in edges:
            d[edge[0]].append(edge[1])
            d[edge[1]].append(edge[0])
               
        dm = None
        vis = [0 for _ in range(len(edges)*2+1)]
        vi = 0
        def chk_tree():
            nonlocal vi
            #print("dm",dm)
            vi += 1
            vis[1] = vi
            dq = deque([(0,1)])
            cnt = 0
            while dq:
                cnt += 1
                t = dq.popleft()
                cur = t[1]
                #print("cur",cur)
                for next in d[cur]:
                    if (cur == dm[0] and next == dm[1]) or (cur == dm[1] and next == dm[0]) or next == t[0]:
                        continue
                    if vis[next] == vi:
                        return False
                    vis[next] = vi
                    dq.append((cur,next))
            if cnt == len(edges):
                return True
            return False
        
        for i in range(len(edges)-1,-1,-1):
            dm = edges[i]
            if chk_tree():
                return dm