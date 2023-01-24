class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        ans = 0
        
        n = len(board)
        d = {}
        for i in range(n):
            for j in range(n):
                cur = n*(n-i) - (j if n%2 == i%2 else n-j-1)
                if board[i][j] != -1:
                    d[cur] = board[i][j]
        
        vis = defaultdict(lambda: -1)
        vis[1] = 0
        dq = deque([1])
        while dq:
            cur = dq.popleft()
            for ncur in range(cur+1, cur+7):
                if ncur > n*n:
                    continue
                if ncur in d:
                    ncur = d[ncur]
                if ncur in vis:
                    continue
                vis[ncur] = vis[cur] + 1
                dq.append(ncur)
        
        return vis[n*n]