class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        ans = -1

        dy,dx = [-1,0,1,0],[0,1,0,-1]

        m,n = len(classroom),len(classroom[0])

        dq = deque()
        ld = {}
        lcnt = 0
        vis = defaultdict(lambda:-1)

        def setup():
            nonlocal lcnt
            for i in range(m):
                for j in range(n):
                    if classroom[i][j] == 'S':
                        vis[(i,j,0)] = energy
                        dq.append((i,j,energy,0,0))
                    if classroom[i][j] == 'L':
                        ld[(i,j)] = lcnt
                        lcnt += 1
        setup()
        # print(ld)

        while dq:
            i,j,e,dis,sta = dq.popleft()
            # print(i,j,e,dis,sta,vis)
            if sta == (1<<lcnt)-1:
                ans = dis
                break
            if e == 0:
                continue
            for di in range(4):
                ni,nj = i+dy[di],j+dx[di]
                # print(ni,nj)
                if ni<0 or nj<0 or ni>=m or nj>=n or classroom[ni][nj] == 'X':
                    continue
                nsta = sta
                if (ni,nj) in ld:
                    idx = ld[(ni,nj)]
                    nsta |= (1<<idx)
                ne = e-1
                if classroom[ni][nj] == 'R':
                    ne = energy
                if vis[(ni,nj,nsta)] >= ne:
                    # print(ni,nj,ne,"e conti")
                    continue
                vis[(ni,nj,nsta)] = ne
                dq.append((ni,nj,ne,dis+1,nsta))

        return ans