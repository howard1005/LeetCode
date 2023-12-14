class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        r,c = len(grid),len(grid[0])
        rd,cd = defaultdict(int),defaultdict(int)
        
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    rd[i] += 1
                else:
                    rd[i] -= 1
        
        for j in range(c):
            for i in range(r):
                if grid[i][j]:
                    cd[j] += 1
                else:
                    cd[j] -= 1
                    
        ans = [[0 for _ in range(c)] for _ in range(r)]
        
        for i in range(r):
            for j in range(c):
                ans[i][j] = rd[i]+cd[j]
                
        return ans
                    