from heapq import heappush,heappop
from sortedcontainers import SortedList

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ansl = [-1 for _ in range(len(queries))]
        
        sl = SortedList()

        hq = []
        for i,h in enumerate(heights):
            heappush(hq,(-h,i))

        def update_sl(v):
            while hq and -hq[0][0] > v:
                h,i = heappop(hq)
                h = -h
                sl.add(i)
        
        
        ql = [(i,a,b) for i,(a,b) in enumerate(queries)]
        ql.sort(key=lambda x: -max(heights[x[1]],heights[x[2]]))
        # print(ql)

        for i,a,b in ql:
            if a == b:
                ansl[i] = a
                continue
            a,b = min(a,b),max(a,b)
            if heights[a] < heights[b]:
                ansl[i] = b
                continue
            mxh = max(heights[a],heights[b])
            update_sl(mxh)
            j = sl.bisect_left(b+1)
            # print(i,a,b,j,len(sl))
            if j < len(sl):
                ansl[i] = sl[j]

        return ansl