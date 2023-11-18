class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        cums = [nums[0]]
        for n in nums[1:]:
            cums.append(cums[-1]+n)
            
        def valid(i,mi):
            n = nums[i]
            return n*(i-mi) - (cums[i]-(cums[mi] if mi>=0 else 0)) <= k
            
        def proc(i):
            ret = 0
            n = nums[i]
            lo,hi = -1,i
            while lo<=hi:
                mi = (lo+hi)//2
                if valid(i,mi):
                    ret = max(ret,i-mi)
                    hi = mi - 1
                else:
                    lo = mi + 1
            return ret
        
        ans = 0
        for i in range(len(nums)):
            ans = max(ans,proc(i))
            
        return ans