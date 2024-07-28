class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:

        ed = defaultdict(list)
        for a,b in edges:
            ed[a].append(b)
            ed[b].append(a)

        def bfs():
            retd = set()
            vis = {}
            dq = deque()
            vis[1] = 0
            dq.append((1,0))
            while dq:
                i,c = dq.popleft()
                if i == n:
                    retd.add(c)
                for j in ed[i]:
                    if j not in vis:
                        vis[j] = c+1
                        dq.append((j,c+1))
                    elif vis[j] == c:
                        dq.append((j,c+1))
            return retd

        rd = bfs()
        
        mn = max(rd) if len(rd) == 2 else max(rd)+2

        ans = 0

        while mn:
            m = ans//change
            if m&1: # red
                ans = (m+1)*change
            ans += time
            mn -= 1

        return ans
                        


            