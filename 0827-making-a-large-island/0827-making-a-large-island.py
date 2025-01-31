from collections import deque,defaultdict

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        dy,dx = [-1,0,1,0],[0,1,0,-1]
        h,w = len(grid),len(grid[0])
        vis = [[0 for _ in range(w)] for _ in range(h)]
        d = defaultdict(int)
        
        def bfs(cury,curx,flag):
            dq = deque()
            d[flag] += 1
            vis[cury][curx] = flag
            dq.append((cury,curx))
            while dq:
                y,x = dq.popleft()
                for di in range(4):
                    ny,nx = y+dy[di],x+dx[di]
                    if ny<0 or nx<0 or ny>=h or nx>=w or vis[ny][nx]==flag or grid[ny][nx]==0:
                        continue
                    d[flag] += 1
                    vis[ny][nx] = flag
                    dq.append((ny,nx))
    
        flag = 1
        for y in range(h):
            for x in range(w):
                if grid[y][x]==1 and vis[y][x]==0:
                    bfs(y,x,flag)
                    flag += 1
        ans = 0
        if d:
            ans = max(d.values())
        
        for y in range(h):
            for x in range(w):
                t = 1
                st = set()
                if grid[y][x]==0:
                    for di in range(4):
                        ny,nx = y+dy[di],x+dx[di]
                        if ny<0 or nx<0 or ny>=h or nx>=w or grid[ny][nx]==0:
                            continue
                        st.add(vis[ny][nx])
                    while st:
                        t += d[st.pop()]
                    ans = max(ans,t)
        
        return ans
    