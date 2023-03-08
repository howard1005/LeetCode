import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def chk(k):
            cnt = 0
            for pile in piles:
                cnt += math.ceil(pile/k)
                if cnt > h:
                    return False
            return True
        
        ans = float('inf')
        lo,hi = 1,100000000000000
        while lo <= hi:
            mi = (lo+hi)//2
            if chk(mi):
                hi = mi-1
                ans = min(ans, mi)
            else:
                lo = mi+1
        return ans
                