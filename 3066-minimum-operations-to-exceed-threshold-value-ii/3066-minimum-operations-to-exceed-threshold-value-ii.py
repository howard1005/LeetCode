from heapq import heappop,heappush

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0

        hq = []

        for n in nums:
            heappush(hq,n)
        
        while hq and hq[0] < k:
            ans += 1
            x,y = heappop(hq),heappop(hq)
            z = min(x, y) * 2 + max(x, y)
            heappush(hq,z)

        return ans
        