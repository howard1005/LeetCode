class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
        dy,dx = [-1,0,1,0],[0,1,0,-1]

        n = len(grid)

        ids = []
        ed = defaultdict(set)

        def get_idx2(r,c):
            idx = 2*(r*n+c)
            return idx,idx+1

        def get_in_idx(r,c,in_di):
            idx1,idx2 = get_idx2(r,c)
            s = grid[r][c]
            if s == '\\':
                if in_di in [0,1]:
                    return idx1
                else:
                    return idx2     
            elif s == '/':
                if in_di in [1,2]:
                    return idx1
                else:
                    return idx2    
            return idx1
            
        def conn(r,c,idx,dis):
            for di in dis:
                nr,nc = r+dy[di],c+dx[di]
                if nr<0 or nc<0 or nr>=n or nc>=n:
                    continue
                tidx = get_in_idx(nr,nc,di)
                ed[idx].add(tidx)
                ed[tidx].add(idx)

        for i in range(n):
            for j in range(n):
                idx1,idx2 = get_idx2(i,j)
                s = grid[i][j]
                if s == '\\':
                    ids.extend([idx1,idx2])
                    conn(i,j,idx1,[2,3])
                    conn(i,j,idx2,[0,1])
                elif s == '/':
                    ids.extend([idx1,idx2])
                    conn(i,j,idx1,[0,3])
                    conn(i,j,idx2,[1,2])
                else:
                    ids.append(idx1)
                    conn(i,j,idx1,[0,1,2,3])
        
        vis = set()
        def bfs(idx):
            dq = deque()
            vis.add(idx)
            dq.append(idx)
            while dq:
                idx = dq.popleft()
                for nidx in ed[idx]:
                    if nidx in vis:
                        continue
                    vis.add(nidx)
                    dq.append(nidx)

        ans = 0
        for idx in ids:
            if idx not in vis:
                ans += 1
                bfs(idx)

        return ans
        