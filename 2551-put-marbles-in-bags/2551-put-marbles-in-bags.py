from heapq import heappush,heappop

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if len(weights) <= 2:
            return 0
        
        def proc(o,kk):
            ret = weights[0] + weights[-1]
            hq = []
            for i in range(len(weights)-1):
                heappush(hq,(o*(weights[i]+weights[i+1])))
                
            while hq and kk:
                w = o*heappop(hq)
                ret += w
                kk -= 1
            return ret
                    
        return abs(proc(1,k-1) - proc(-1,k-1))
        