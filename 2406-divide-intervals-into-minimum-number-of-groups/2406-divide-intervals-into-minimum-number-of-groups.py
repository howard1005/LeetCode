from heapq import heappush,heappop

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        ans=0
        
        intervals.sort()

        idx = 0
        h = []
        
        for s,e in intervals:
            if h and h[0][0] < s:
                _,i = heappop(h)
                heappush(h,(e,i))
            else:
                i = idx
                heappush(h,(e,i))
                idx += 1
        
        ans = len(h)

        return ans
        
        