class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        ps = [0] * (n + 1)
        for i in range(n):
            ps[i + 1] = ps[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]
        l = [[0] * n for _ in range(n)]
        r = [[0] * n for _ in range(n)]

        for i in range(n):
            l[i][i] = stoneValue[i]
            r[i][i] = stoneValue[i]

        for a in range(n - 1, -1, -1):
            p = a + 1

            for b in range(a + 1, n):
                target = ps[a] + ps[b + 1]

                while p <= b and ps[p] * 2 < target:
                    p += 1

                ret = 0

                if p > b:
                    ret = l[a][b - 1]
                else:
                    if ps[p] * 2 == target:
                        ret = max(ret, l[a][p - 1])
                    elif p >= a + 2:
                        ret = max(ret, l[a][p - 2])

                    ret = max(ret, r[p][b])

                dp[a][b] = ret

                tot = ps[b + 1] - ps[a]

                l[a][b] = max(
                    l[a][b - 1],
                    tot + dp[a][b]
                )

                r[a][b] = max(
                    r[a + 1][b],
                    tot + dp[a][b]
                )

        return dp[0][n - 1]