class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        mxh = 0
        hcnt = 0
        prev = 1
        for h in hBars:
            if prev+1 == h:
                hcnt += 1
            else:
                hcnt = 1
            prev = h
            mxh = max(mxh,hcnt)

        vBars.sort()
        mxv = 0
        vcnt = 0
        prev = 1
        for v in vBars:
            if prev+1 == v:
                vcnt += 1
            else:
                vcnt = 1
            prev = v
            mxv = max(mxv,vcnt)

        # print(mxh,mxv)

        ans = (min(mxh,mxv)+1)**2

        return ans
        