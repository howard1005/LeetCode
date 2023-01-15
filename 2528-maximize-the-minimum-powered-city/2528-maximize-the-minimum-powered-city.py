from collections import deque

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        ans = 0
        
        l = [0 for _ in range(len(stations))]
        l[0] = sum(stations[:r+1])
        for i in range(1,len(stations)):
            ai,bi = i-r-1,i+r
            a = stations[ai] if ai>=0 else 0
            b = stations[bi] if bi<len(stations) else 0
            l[i] = l[i-1]-a+b
            
        # print("l:{}".format(l))
        
        def valid(p):
            # print("\np:{}".format(p))
            kk = k
            cor = 0
            dq = deque()
            for i in range(len(l)):
                if dq and dq[0][1] < i:
                    cor -= dq.popleft()[0]
                if l[i]+cor < p:
                    c = p-l[i]-cor
                    kk -= c
                    if kk < 0:
                        return False
                    cor += c
                    dq.append((c,i+2*r))
                # print("{} ".format(l[i]+cor),end="")
            return True
        
        lo,hi = 0,10**11
        while lo<=hi:
            mi = (lo+hi)//2
            if valid(mi):
                ans = mi
                lo = mi+1
            else:
                hi = mi-1
                    
        return ans     
            