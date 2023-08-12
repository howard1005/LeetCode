class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r_len = len(obstacleGrid)
        c_len = len(obstacleGrid[0])
        if r_len == 1 and c_len == 1:
            if obstacleGrid[0][0]:
                return 0
            else:
                return 1
        bd = [[0 for _ in range(c_len)] for _ in range(r_len)]
        bd[0][0] = 1
        
        for n in range(r_len + c_len - 1):
            for y in range(n):
                x = n - y - 1
                #print(y,x)
                if y<0 or x<0 or y>=r_len or x>=c_len or obstacleGrid[y][x]:
                    continue
                if y+1<r_len and obstacleGrid[y+1][x] == 0:
                    bd[y+1][x] += bd[y][x]
                if x+1<c_len and obstacleGrid[y][x+1] == 0:
                    bd[y][x+1] += bd[y][x]
                    
        #for r in bd:
        #    print(r)
                    
        return bd[r_len-1][c_len-1]