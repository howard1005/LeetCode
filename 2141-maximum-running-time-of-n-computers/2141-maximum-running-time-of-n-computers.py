class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        ans = 0
        
        def valid(c):
            i,j = 0,0
            need = c
            remain = min(batteries[j],c)
            while i<n and j<len(batteries):
                if need < remain:
                    remain -= need
                    need = c
                    i += 1
                elif need > remain:
                    need -= remain
                    if j == len(batteries)-1:
                        break
                    remain = min(batteries[j+1],c)
                    j += 1
                else:
                    need = c
                    i += 1
                    if j == len(batteries)-1:
                        break
                    remain = min(batteries[j+1],c)
                    j += 1
            return i == n
                    
        
        lo,hi = 0,max(batteries)*len(batteries)
        while lo<=hi:
            mi = (lo+hi)//2
            if valid(mi):
                ans = max(ans,mi)
                lo = mi + 1
            else:
                hi = mi - 1
                
        return ans