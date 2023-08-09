from heapq import heappush,heappop

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:       
        ans = inf
        
        nums.sort()
        
        def valid(t):
            cnt = 0
            i = 0
            while i<len(nums)-1:
                a = abs(nums[i]-nums[i+1])
                if a <= t:
                    cnt += 1
                    if cnt >= p:
                        return True
                    i += 2
                else:
                    i += 1
            return cnt >= p


        lo,hi = 0,1000000000
        while lo<=hi:
            mi = (lo+hi)//2
            if valid(mi):
                ans = min(ans,mi)
                hi = mi - 1
            else:
                lo = mi + 1
                
        return ans if ans != inf else 0