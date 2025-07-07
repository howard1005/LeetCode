from heapq import heappush,heappop

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        ans = 0

        events.sort(reverse=True)

        hq = []

        for d in range(1,100001):
            while events and events[-1][0] <= d:
                a,b = events.pop()
                heappush(hq,(b,a))
            while hq and hq[0][0] < d:
                heappop(hq)
            if hq:
                ans += 1
                heappop(hq)
        
        return ans