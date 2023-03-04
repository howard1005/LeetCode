class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        
        wi = -1
        mni = -1
        mxi = -1
        
        for i in range(len(nums)):
            n = nums[i]
            if n < minK or maxK < n:
                wi = i
            if n == minK:
                mni = i
            if n == maxK:
                mxi = i
            r = min(mni,mxi)-wi
            if r > 0:
                ans += r
        
        return ans