class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        ans = inf
        
        def valid(t):
            cum = 0
            for q in quantities:
                cum += q//t + (1 if q%t else 0)
                if cum > n:
                    return False
            return True
                
        
        lo,hi = 1,max(quantities)
        while lo<=hi:
            mi = (lo+hi)//2
            if valid(mi):
                ans = min(ans,mi)
                hi = mi - 1
            else:
                lo = mi + 1

        return -1 if ans == inf else ans