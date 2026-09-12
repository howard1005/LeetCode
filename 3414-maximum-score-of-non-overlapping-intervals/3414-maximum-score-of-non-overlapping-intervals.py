from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        ans = []

        le = len(intervals)

        l = [(a,b,c,i) for i,(a,b,c) in enumerate(intervals)]
        l.sort()
        # print(l)

        dp = [[0 for _ in range(4)] for _ in range(le)]
        dpl = [[None for _ in range(4)] for _ in range(le)]

        for j in range(4):
            dp[-1][j] = l[-1][2]
            dpl[-1][j] = [l[-1][3]]

        for i in range(le-2,-1,-1):
            for j in range(4):
                r1 = dp[i+1][j]
                k = bisect_right(l,l[i][1],key=lambda x: x[0])
                r2 = l[i][2] + (dp[k][j+1] if k < le and j<3 else 0)

                p1 = dpl[i+1][j]
                p2 = sorted(
                    [l[i][3]] +
                    (dpl[k][j+1] if k < le and j < 3 else [])
                )

                if r1 < r2 or (r1 == r2 and p2 < p1):
                    dp[i][j] = r2
                    dpl[i][j] = p2
                else:
                    dp[i][j] = r1
                    dpl[i][j] = p1
                
        # for r in dp:
        #     print(r)

        # print()
        # for r in dpi:
        #     print(r)

        # print()

        ans = dpl[0][0]

        return ans