from heapq import heappush,heappop

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        ans = 0
        
        hq = []
        for n in nums:
            heappush(hq,-n)
        tot = sum(nums)
        cum = tot
        while cum > tot/2:
            n = -heappop(hq)
            cum -= n/2
            heappush(hq,-n/2)
            ans += 1
        
        return ans