from heapq import heappush,heappop

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        ans = 0

        d = defaultdict(list)

        for i,(a,b) in enumerate(conflictingPairs):
            if a>b:
                a,b = b,a
            d[b].append((i,a,b))

        hq = []
        dd = defaultdict(lambda:[None,None])
        

        for i in range(1,n+1):
            for idx,a,b in d[i]:
                heappush(hq,(-a,b,idx))
            idx,a,b = -1,0,0
            if len(hq) >= 2:
                t = heappop(hq)
                _a,_b,_idx = hq[0]
                _a = -_a
                idx,a,b = _idx,_a,_b
                heappush(hq,t)
            dd[i][1] = (idx,a,b)
            if hq:
                _a,_b,_idx = hq[0]
                _a = -_a
                idx,a,b = _idx,_a,_b
            dd[i][0] = (idx,a,b)

        # print(dd)

        cum = 0
        for i,l in dd.items():
            idx,a,b = l[0]
            cum += i-a

        # print(cum)

        rdd = defaultdict(int)

        for i,l in dd.items():
            idx1,a1,b1 = l[0]
            idx2,a2,b2 = l[1]
            rdd[idx1] += a1-a2

        # print(rdd)

        ans = cum + max(rdd.values())
            
        return ans