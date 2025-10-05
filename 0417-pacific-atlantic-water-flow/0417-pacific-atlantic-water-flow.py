from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dy,dx = [-1,0,1,0],[0,1,0,-1]
        r,c = len(heights),len(heights[0])
        mp = [[-1 for _ in range(c)] for _ in range(r)]
        mpp = []
        
        def dfs(y,x,i):
            if y == 0 or x == 0:
                mpp[i][1][0] = 1
            if y == r-1 or x == c-1:
                mpp[i][1][1] = 1
            mp[y][x] = i
            mpp[i][2].append((y,x))
            for di in range(4):
                ny,nx = y+dy[di],x+dx[di]
                if ny<0 or nx<0 or ny>=r or nx>=c:
                    continue
                if heights[y][x] > heights[ny][nx]:
                    mpp[i][0] += 1
                if mp[ny][nx] == -1 and heights[y][x] == heights[ny][nx]:
                    dfs(ny,nx,i)

        
        dq = deque()
        for y in range(r):
            for x in range(c):
                if mp[y][x] == -1:
                    mpp.append([0,[0,0],[]])
                    dfs(y,x,len(mpp)-1)
                    if mpp[-1][0] == 0:
                        dq.append(len(mpp)-1)
        
        
        while dq:
            i = dq.popleft()
            for y,x in mpp[i][2]:
                for di in range(4):
                    ny,nx = y+dy[di],x+dx[di]
                    if ny<0 or nx<0 or ny>=r or nx>=c:
                        continue
                    j = mp[ny][nx]
                    if heights[y][x] < heights[ny][nx]:
                        mpp[j][1][0] |= mpp[i][1][0]
                        mpp[j][1][1] |= mpp[i][1][1]
                        mpp[j][0] -= 1
                        if mpp[j][0] == 0:
                            dq.append(j)
        
        ans = []
        for t in mpp:
            if t[1] == [1,1]:
                ans.extend(t[2])
        
        return ans
        