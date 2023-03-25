class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        
        d = defaultdict(list)
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)
        
        vis = {}
        def bfs(s):
            ret = 0
            vis[s] = 1
            dq = deque([s])
            while dq:
                cur = dq.popleft()
                ret += 1
                for ncur in d[cur]:
                    if ncur not in vis:
                        vis[ncur] = 1
                        dq.append(ncur)
            return ret
        
        for i in range(n):
            if i not in vis:
                cnt = bfs(i)
                ans += cnt*(n-cnt)
        
        return ans//2