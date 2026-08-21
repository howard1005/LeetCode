from itertools import combinations
from math import lcm

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # 1,2,3,5,7,11,13,17,19,23

        ans = 0


        def multiples_union(l, m):
            count = 0

            for k in range(1, len(l) + 1):
                for c in combinations(l, k):
                    count += (-1) ** (k + 1) * (m // lcm(*c))

            last = max(((m // x) * x for x in l if x <= m), default=0)
            return count, last
            
        def valid(m):
            count, last = multiples_union(coins,m)
            if count < k:
                return 1,last
            if count > k:
                return -1,last
            return 0,last
            
        lo,hi = 0,k*max(coins)
        while lo<=hi:
            mi = (lo+hi)//2
            v,mx = valid(mi)
            if v == 1:
                lo = mi+1
            elif v == -1:
                hi = mi-1
            else:
                ans = mx
                break

        return ans
                