from bisect import bisect_right
from heapq import heappush,heappop

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        ans = [0 for _ in range(len(people))]
        
        flowers.sort()
        
        marks = [[] for _ in range(len(flowers))]
        
        for i,t in enumerate(people):
            j = bisect_right(flowers, t, key=lambda x:x[0])
            if j > 0:
                marks[j-1].append((i,t))
                
        for l in marks:
            l.sort(key=lambda x: x[1])
            
        hq = []
        for i,(a,b) in enumerate(flowers):
            heappush(hq,b)
            l = marks[i]
            if l:
                for pi,t in l:
                    while hq and hq[0] < t:
                        heappop(hq)
                    ans[pi] = len(hq)

        return ans