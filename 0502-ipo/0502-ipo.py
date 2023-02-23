from heapq import heappush,heappop

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        ans = 0
        
        l = [(c,p) for p,c in zip(profits,capital)]
        l.sort()
        
        hq = []
        
        i = 0
        while k:
            while i < len(l):
                if w < l[i][0]:
                    break
                heappush(hq, -l[i][1])
                i += 1
            if not hq:
                break
            w -= heappop(hq)
            k -= 1
        
        ans = w
        
        return ans