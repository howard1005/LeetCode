from heapq import heappush,heappop

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = defaultdict(int)
        
        for n in arr:
            d[n] += 1
            
        hq = []
        for n,cnt in d.items():
            heappush(hq, (cnt,n))
        
        while k:
            cnt,n = heappop(hq)
            cnt -= 1
            if cnt:
                heappush(hq, (cnt,n))
            k -= 1
        
        return len(hq)