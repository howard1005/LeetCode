class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        dy,dx = [-1,0,1,0],[0,1,0,-1]

        dp = {}

        def find_zero(state):
            for i in range(len(state)):
                for j in range(len(state[0])):
                    if state[i][j] == 0:
                        return i,j 

        def valid(state):
            v = 1
            for i in range(len(state)):
                for j in range(len(state[0])):
                    if state[i][j] != v:
                        return False
                    v = (v+1)%6
            return True

        def dtuple(l):
            retl = []
            for ll in l:
                retl.append(tuple(ll))
            return tuple(retl)


        def bfs(state):

            dq = deque([(state,0)])

            while dq:
                st,cnt = dq.popleft()
                # print(st,cnt)
                if valid(st):
                    return cnt
                zi,zj = find_zero(st)
                # print(zi,zj)
                for di in range(4):
                    nzi,nzj = zi+dy[di],zj+dx[di]
                    if nzi<0 or nzj<0 or nzi>=2 or nzj>=3:
                        continue
                    cst = [st[0][:],st[1][:]]
                    cst[zi][zj],cst[nzi][nzj] = cst[nzi][nzj],cst[zi][zj]
                    t = dtuple(cst)
                    if t in dp:
                        continue
                    dp[t] = cnt+1
                    dq.append((cst,cnt+1))
            
            return -1

        ans = bfs(board)

        return ans
            