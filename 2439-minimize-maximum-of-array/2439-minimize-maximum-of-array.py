class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = inf
        
        def chk(mi):
            cnt = 0
            for n in nums[::-1]:
                cnt += n - mi
                cnt = max(cnt,0)                            
            return cnt == 0
        
        lo,hi = 0,1000000000
        while lo<=hi:
            mi = (lo+hi)//2
            if chk(mi):
                ans = min(ans,mi)
                hi = mi - 1
            else:
                lo = mi + 1
                
        return ans