class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        ans = 0
        
        a,b = index,n-index-1
        
        def sigma(k):
            return (k+1)*k//2
        
        def valid(t):
            return maxSum-n >= sigma(t)*2-t-sigma(max(0,t-1-a))-sigma(max(0,t-1-b))
        
        lo,hi = 0,maxSum
        while lo <= hi:
            mi = (lo+hi)//2
            if valid(mi):
                ans = max(ans,mi+1)
                lo = mi + 1
            else:
                hi = mi - 1
        
        return ans