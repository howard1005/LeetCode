class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        ans = inf
        
        def valid(v):
            t = 0
            for d in dist[:-1]:
                t += ceil(d/v)
            t += dist[-1]/v
            return t<=hour
        
        cum = sum(dist)        
        lo = max(1,cum//hour)
        hi = lo*len(dist)*100
        while lo<=hi:
            mi = int((lo+hi)//2)
            if valid(mi):
                ans = min(ans,mi)
                hi = mi - 1
            else:
                lo = mi + 1
        
        return -1 if ans == inf else ans