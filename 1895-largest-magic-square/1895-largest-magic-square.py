class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        ans = 0

        m,n = len(grid),len(grid[0])

        cm = [[[0]*2 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                cm[i][j][0] = grid[i][j]
                cm[i][j][0] += cm[i][j-1][0] if j-1>=0 else 0

        for j in range(n):
            for i in range(m):
                cm[i][j][1] = grid[i][j]
                cm[i][j][1] += cm[i-1][j][1] if i-1>=0 else 0

        # for r in cm:
        #     print(r)
        
            
        def valid(sy,sx,le):
            # print(sy,sx,le)
            i,j = sy,sx
            r = 0
            while i<sy+le and i<m and j<n:
                r += grid[i][j]
                i+=1
                j+=1
            base = r
            # print('base',base)

            i,j = sy,sx+le-1
            r = 0
            while i<sy+le and i<m and j<n and j>=0:
                r += grid[i][j]
                i+=1
                j-=1
            # print('diag',r)
            if r != base:
                return False
            
            
            for i in range(sy,min(m,sy+le)):
                r = (cm[i][sx+le-1][0] if sx+le-1<n else cm[i][-1][0])-(cm[i][sx-1][0] if sx>0 else 0)
                # print('i',i,r)
                if r != base:
                    return False

            for j in range(sx,min(n,sx+le)):
                r = (cm[sy+le-1][j][1] if sy+le-1<m else cm[-1][sx][1])-(cm[sy-1][j][1] if sy>0 else 0)
                # print('j',j,r)
                if r != base:
                    return False

            return True

        for le in range(min(m,n),0,-1):
            for i in range(m-le+1):
                for j in range(n-le+1):
                    if valid(i,j,le):
                        return le
                    

        return ans