class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        a = 0
        for i in range(x,x+k):
            ii = x+k-1-a
            # print(i,ii,a)
            if i >= ii:
                break
            for j in range(y,y+k):
                grid[i][j],grid[ii][j] = grid[ii][j],grid[i][j]
            a += 1
        return grid