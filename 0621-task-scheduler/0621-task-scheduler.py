from heapq import heappush,heappop

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ans = 0
        
        gt = 0
        
        idle_q = [] # (-cnt,c) 
        busy_q = [] # (time,cnt,c)
        
        tot = 0
        d = defaultdict(int)
        for c in tasks:
            d[c] += 1
            tot += 1
        
        for c,cnt in d.items():
            heappush(idle_q,(-cnt,c))
            
        while tot:
            
            while busy_q and busy_q[0][0] < gt:
                t,cnt,c = heappop(busy_q)
                if cnt:
                    heappush(idle_q,(-cnt,c))
            
            if idle_q:
                cnt,c = heappop(idle_q)
                tot -= 1
                if cnt+1:
                    heappush(busy_q,(gt+n,-(cnt+1),c))
            
            gt += 1
        
        ans = gt
        
        return ans