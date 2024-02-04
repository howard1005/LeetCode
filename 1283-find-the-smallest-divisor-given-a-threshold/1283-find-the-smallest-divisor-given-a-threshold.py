class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        ans = -1
        
        def valid(m):
            cum = 0
            for n in nums:
                cum += n//m + (1 if n%m else 0)
            return cum<=threshold
        
        lo,hi = 1,max(nums)
        while lo<=hi:
            mi = (lo+hi)//2
            if valid(mi):
                ans = mi
                hi = mi-1
            else:
                lo = mi+1
                
        return ans