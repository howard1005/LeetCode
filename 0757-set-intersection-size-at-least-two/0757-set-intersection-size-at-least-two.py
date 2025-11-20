from heapq import heappush,heappop

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        ans = 0

        hq = []

        sd = set()

        intervals.sort()
        # print(intervals)

        l = []
        for i,(a,b) in enumerate(intervals):
            # l.append((a,i,1))
            l.append((b,i,0))
        l.sort()
        # print(l)

        def getv(v):
            while v in sd:
                v -= 1
            return v

        for v,i,f in l:
            a,b = intervals[i]
            c,d = -1,-1
            if hq:
                c = abs(heappop(hq))
            if hq:
                d = abs(heappop(hq))
            
            need = 2
            if a <= c and c <= b:
                need -= 1
            if a <= d and d <= b:
                need -= 1

            if need:
                v = getv(b)
                need -= 1
                sd.add(v)
                heappush(hq,-v)
            if need:
                v = getv(b)
                need -= 1
                sd.add(v)
                heappush(hq,-v)

            if c != -1:
                heappush(hq,-c)
            if d != -1:
                heappush(hq,-d)
            

            # print(sd,hq)

        ans = len(sd)
            

        return ans