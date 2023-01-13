from collections import deque

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        ans = 1
        
        l = [0 for _ in range(len(parent))]
        for p in parent:
            if p != -1:
                l[p] += 1
                
        dq = deque()
        for i,c in enumerate(l):
            if c == 0:
                dq.append(i)
        
        pl = [[] for _ in range(len(parent))]
        while dq:
            i = dq.popleft()
            tl = pl[i]
            # print(i,tl)
            up = 1
            if tl:
                tl.sort(reverse=True)
                ans = max(ans,sum(tl[:2])+1)
                up += tl[0]
            p = parent[i]
            if p != -1:
                if s[p] != s[i]:
                    pl[p].append(up)
                l[p] -= 1
                if l[p] == 0:
                    dq.append(p)
        
        return ans