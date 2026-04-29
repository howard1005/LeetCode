class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        ans = 0

        n = len(grid)
        
        @cache
        def dfs(ppis,pi,j):
            if j >= n:
                return 0
            ret = 0

            t = 0
            for i in range(n):
                if i<=pi:
                    t += grid[i][j]
                else:
                    break
            
            pt = 0
            for ni in range(-1,n):
                if ni>=0:
                    t -= grid[ni][j]
                if ppis and ni>pi and j-1>=0:
                    pt += grid[ni][j-1]
                    
                ret = max(ret,dfs(0,ni,j+1)+t+pt,dfs(1,ni,j+1)+pt)

            return ret


        ans = dfs(1,-1,0)

        return ans