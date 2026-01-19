class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        ans = 0

        m,n = len(mat),len(mat[0])
        # print(m,n)
        
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                dp[i][j] = mat[i][j]
                if i-1>=0:
                    dp[i][j] += dp[i-1][j]
                if j-1>=0:
                    dp[i][j] += dp[i][j-1]
                if i-1>=0 and j-1>=0:
                    dp[i][j] -= dp[i-1][j-1]
        # for r in dp:
        #     print(r)

        def area(a,b,c,d):
            ret = dp[c][d]
            if b-1>=0:
                ret -= dp[c][b-1]
            if a-1>=0:
                ret -= dp[a-1][d]
            if a-1>=0 and b-1>=0:
                ret += dp[a-1][b-1]
            return ret

        def valid(le):
            for i in range(m-le+1):
                for j in range(n-le+1):
                    a = area(i,j,i+le-1,j+le-1)
                    # print(le,i,j,a)
                    if a <= threshold:
                        return True
            return False

        lo,hi = 1,min(m,n)
        while lo<=hi:
            mi = (lo+hi)//2
            v = valid(mi)
            if v:
                ans = max(ans,mi)
                lo = mi+1
            else:
                hi = mi-1

        return ans
            