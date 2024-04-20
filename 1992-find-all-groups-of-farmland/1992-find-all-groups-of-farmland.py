class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        
        dy,dx = [-1,0,1,0],[0,1,0,-1]
        m,n = len(land),len(land[0])
        vis = {}
        
        def bfs(y,x):
            tl,br = (y,x),(y,x)
            
            dq = deque()
            vis[(y,x)] = 1
            dq.append((y,x))
            
            while dq:
                y,x = dq.popleft()
                tl,br = min(tl,(y,x)),max(br,(y,x))
                for di in range(4):
                    ny,nx = y+dy[di],x+dx[di]
                    if ny<0 or nx<0 or ny>=m or nx>=n or land[ny][nx] == 0 or (ny,nx) in vis:
                        continue
                    vis[(ny,nx)] = 1
                    dq.append((ny,nx))
            
            return list(tl+br)

        
        for i in range(m):
            for j in range(n):
                if (i,j) not in vis and land[i][j]:
                    ans.append(bfs(i,j))

        return ans
        