class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = 0
        
        vis = {}
        def bfs(si):
            vis[si] = 1
            dq = deque([si])
            while dq:
                i = dq.popleft()
                for j,c in enumerate(isConnected[i]):
                    if c and j not in vis:
                        vis[j] = 1
                        dq.append(j)
        
        for i in range(len(isConnected)):
            if i not in vis:
                ans += 1
                bfs(i)
        
        return ans