class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ans = inf

        def valid(mi):
            cnt = 0
            for r in ranks:
                cnt += int(sqrt(mi//r))
            return cnt >= cars

        lo,hi = 1,max(ranks)*cars*cars

        while lo<=hi:
            mi = (lo+hi)//2
            if valid(mi):
                ans = min(ans,mi)
                hi = mi-1
            else:
                lo = mi+1

        return ans

            

        
            