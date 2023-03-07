class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        ans = 0
        
        def chk(m):
            return sum([m//t for t in time]) >= totalTrips
        
        lo,hi = 0,10**14
        while lo<=hi:
            mi = (lo+hi)//2
            flag = chk(mi)
            if flag:
                ans = mi
                hi = mi-1
            else:
                lo = mi+1
                
        return ans
        