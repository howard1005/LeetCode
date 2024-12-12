from heapq import heappush,heappop

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        hq = []
        for g in gifts:
            heappush(hq,-g)
        
        for _ in range(k):
            g = -heappop(hq)
            heappush(hq,-int(sqrt(g)))

        return -sum(hq)