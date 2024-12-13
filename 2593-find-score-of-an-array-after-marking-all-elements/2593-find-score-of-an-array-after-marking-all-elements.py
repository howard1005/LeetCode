from heapq import heappush,heappop

class Solution:
    def findScore(self, nums: List[int]) -> int:
        ans = 0

        hq = []
        
        for i,n in enumerate(nums):
            heappush(hq,(n,i))
        
        vis = set()

        while hq:
            n,i = heappop(hq)
            if i not in vis:
                vis.add(i-1)
                vis.add(i)
                vis.add(i+1)
                ans += n

        return ans