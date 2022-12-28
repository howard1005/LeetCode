from heapq import heappush,heappop

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        ans = 0
        
        h = []
        for p in piles:
            ans += p
            heappush(h,-p)
        while k:
            p = -heappop(h)
            rm = p//2
            heappush(h,-(p-rm))
            ans -= rm
            k -= 1
            
        return ans