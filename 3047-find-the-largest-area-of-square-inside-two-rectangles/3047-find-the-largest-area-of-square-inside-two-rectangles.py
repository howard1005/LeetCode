class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        ans = 0

        n = len(bottomLeft)

        for i in range(n):
            for j in range(i+1,n):
                sx1,sy1 = bottomLeft[i]
                ex1,ey1 = topRight[i]
                sx2,sy2 = bottomLeft[j]
                ex2,ey2 = topRight[j]

                sx,ex = max(sx1,sx2),min(ex1,ex2)
                if sx>=ex:
                    continue
                sy,ey = max(sy1,sy2),min(ey1,ey2)
                if sy>=ey:
                    continue
                le = min(ex-sx,ey-sy)
                ans = max(ans,le*le)

        return ans