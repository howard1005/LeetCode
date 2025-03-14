class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        ans = 0

        def valid(mi):
            kk = k
            for c in candies:
                kk -= c//mi
            return True if kk<=0 else False
        
        lo,hi = 1,max(candies)
        while lo<=hi:
            mi = (lo+hi)//2
            if valid(mi):
                ans = max(ans,mi)
                lo = mi+1
            else:
                hi = mi-1
                
        return ans