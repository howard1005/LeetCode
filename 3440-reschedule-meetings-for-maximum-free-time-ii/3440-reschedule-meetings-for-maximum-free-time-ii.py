from heapq import heappop,heappush

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        ans = 0

        l = []
        
        last = 0
        for i,(a,b) in enumerate(zip(startTime,endTime)):
            l.append((last,a))
            last = b
        l.append((last,eventTime))

        sl = []
        for i,(a,b) in enumerate(l):
            size = b-a
            if i > 0:
                nsize = sl[-1][0]+size
                ans = max(ans,nsize)
            sl.append((size,i))
        sl.sort(reverse=True)

        tl = sl[:3]
        # print(f"tl : {tl}")
        def fit(i):
            a,b = startTime[i],endTime[i]
            size = b-a
            
            for tsize,j in tl:
                if i != j and i+1 != j and tsize>=size:
                    return l[i+1][1] - l[i][0]

            return -1
            
        for i in range(len(l)-1):
            r = fit(i)
            if r != -1:
                ans = max(ans,r)

        return ans