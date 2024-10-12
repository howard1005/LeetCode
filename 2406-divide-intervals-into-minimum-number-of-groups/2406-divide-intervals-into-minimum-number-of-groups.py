from heapq import heappush,heappop

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        ans=0
        
        intervals.sort()

        h = []
        
        for s,e in intervals:
            if h and h[0] < s:
                heappop(h)
                heappush(h,e)
            else:
                heappush(h,e)
        
        ans = len(h)

        return ans
        
        