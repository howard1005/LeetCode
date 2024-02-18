from heapq import heappush,heappop

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        d = defaultdict(int)
        
        meetings.sort()
        
        aq = []
        uq = []
        
        for i in range(n):
            heappush(aq,i,)
        
        def waitRoom(t,one=False):
            while uq and uq[0][0] <= t:
                a,i = heappop(uq)
                heappush(aq,i)
                if one:
                    break
        
        for s,e in meetings:
            m = e-s
            waitRoom(s)
            if not aq:
                s = uq[0][0]
                waitRoom(s,True)
            i = heappop(aq)
            # print(s,e,i)
            heappush(uq,(s+m,i))
            d[i] += 1
        
        
        l = [(cnt,i) for i,cnt in d.items()]
        l.sort(key=lambda x: (-x[0],x[1]))
        
        # print(l)
        
        return l[0][1]
                