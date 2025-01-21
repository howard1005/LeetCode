class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        ans = inf
        
        n = len(grid[0])

        l,r = [0 for _ in range(n)],[0 for _ in range(n)]
        l[0],r[-1] = grid[1][0],grid[0][-1]
        for i in range(1,n):
            l[i] += l[i-1] + grid[1][i]
        for i in range(n-2,-1,-1):
            r[i] += r[i+1] + grid[0][i]
        
        for i in range(n):
            lmx,rmx = l[i-1] if i else 0,r[i+1] if i < n-1 else 0
            ans = min(ans,max(lmx,rmx))
            
        return ans