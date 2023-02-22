class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        ans = inf
        
        def chk(tw):
            td = days
            cum = 0
            for w in weights:
                if w > tw:
                    return False
                if cum + w <= tw:
                    cum += w
                else:
                    td -= 1
                    if td == 0:
                        return False
                    cum = w
            return td >= 0
        
        lo,hi = 0,10000000
        while lo<=hi:
            mi = (lo+hi)//2
            if chk(mi):
                ans = min(ans,mi)
                hi = mi - 1
            else:
                lo = mi + 1
        
        
        return ans