class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l = [0 for _ in range(len(nums))]
        l[0] = nums[0]
        for i in range(1,len(nums)):
            l[i] = l[i-1]+nums[i]
        
        def chk(target,hi):
            lo = 0
            while lo<=hi:
                mi = (lo+hi)//2
                # print(lo,hi,mi,l[mi],target)
                n = l[mi]
                if n < target:
                    lo = mi+1
                elif n > target:
                    hi = mi-1
                else:
                    return mi
            return -1
        
        ans = float('inf')
        ct = chk(x,len(nums)-1)
        if ct != -1:
            ans = ct+1
        # print('init')
        
        
        cum = 0
        for i in range(len(nums)-1,-1,-1):
            cum += nums[i]
            if x > cum:
                ct = chk(x-cum,i-1)
                if ct != -1:
                    ans = min(ans,ct+1+len(nums)-i)
            elif x == cum:
                ans = min(ans,len(nums)-i)
            else:
                break
        
        if ans == float('inf'):
            ans = -1
        return ans
                
        
        
        