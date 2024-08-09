class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans = 0

        r,c = len(grid),len(grid[0])

        def valid(a,b):
            d = set()
            for i in range(a,a+3):
                cum = 0
                for j in range(b,b+3):
                    d.add(grid[i][j])
                    cum += grid[i][j]
                if cum != 15:
                    return 0
            for i in range(1,10):
                if i not in d:
                    return 0
            for j in range(b,b+3):
                cum = 0
                for i in range(a,a+3):
                    cum += grid[i][j]
                if cum != 15:
                    print(2)
                    return 0
            cum = 0
            for i in range(3):
                cum += grid[a+i][b+i]
            if cum != 15:
                return 0
            cum = 0
            for i in range(3):
                cum += grid[a+i][b+2-i]
            if cum != 15:
                return 0
            return 1

        for i in range(r-2):
            for j in range(c-2):
                ans += valid(i,j)

        return ans
        