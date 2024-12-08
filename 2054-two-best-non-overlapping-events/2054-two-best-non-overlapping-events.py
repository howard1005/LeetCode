from heapq import heappush,heappop

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        ans = max([v for i,(s,e,v) in enumerate(events)])

        sl = [(s,v,i) for i,(s,e,v) in enumerate(events)]
        sl.sort()
        el = [(e,v,i) for i,(s,e,v) in enumerate(events)]
        el.sort()

        hq = []

        j = 0
        for s,v,i in sl:
            while j<len(el) and el[j][0]<s:
                e,ev,ei = el[j]
                heappush(hq,(-ev,ei))
                j += 1
            if hq:
                ans = max(ans,-hq[0][0]+v)

        return ans