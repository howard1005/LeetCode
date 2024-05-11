from heapq import heappush,heappop

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ans = inf

        l = [(w/q,q,w) for q,w in zip(quality,wage)]
        l.sort()

        cum = 0
        hq = []
        for r,q,w in l:
            if len(hq) < k-1:
                cum += q
                heappush(hq, -q)
                continue

            ans = min(ans, cum*w/q+w)

            if hq and q < -hq[0]:
                cum += heappop(hq) + q
                heappush(hq, -q)

        return ans