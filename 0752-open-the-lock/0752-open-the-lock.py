from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        if '0000' == target:
            return 0
        vis = [0 for _ in range(10000)]
        dq = deque()
        vis[0] = 1
        dq.append(('0000',0))
        while dq:
            s,cnt = dq.popleft()
            for i in range(4):
                for j in [-1,1]:
                    n = (int(s[i])+j+10)%10
                    s_next = s[:i]+str(n) +s[i+1:]
                    if vis[int(s_next)] or s_next in deadends:
                        continue
                    if s_next == target:
                        return cnt+1
                    vis[int(s_next)] = 1
                    dq.append((s_next,cnt+1))
        return -1

                
            