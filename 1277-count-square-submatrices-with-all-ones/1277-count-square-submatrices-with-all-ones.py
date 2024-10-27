class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0

        m,n = len(matrix),len(matrix[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        def area(i,j):
            if i<0 or j<0:
                return 0
            return dp[i][j]

        for i in range(m):
            for j in range(n):
                dp[i][j] = matrix[i][j] + area(i-1,j) + area(i,j-1) - area(i-1,j-1)

        def max_side(i,j):
            if matrix[i][j] == 0:
                return 0
            ret = 0
            mn = min(i,j)+1
            lo,hi = 1,mn
            while lo<=hi:
                mi = (lo+hi)//2
                a = area(i,j) - area(i-mi,j) - area(i,j-mi) + area(i-mi,j-mi)
                if a == mi*mi:
                    lo = mi+1
                    ret = max(ret,mi)
                else:
                    hi = mi-1
            return ret

        for i in range(m):
            for j in range(n):
                mxe = max_side(i,j)
                ans += mxe

        return ans