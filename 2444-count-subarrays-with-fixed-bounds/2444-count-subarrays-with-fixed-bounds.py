class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0

        oi,mni,mxi = -1,-1,-1

        for i,n in enumerate(nums):
            if n == minK:
                mni = i
            if n == maxK:
                mxi = i
            if n<minK or n>maxK:
                oi = i
            
            if mni!=-1 and mxi!=-1 and oi<mni and oi<mxi:
                j = min(mni,mxi)
                ans += j-oi

        return ans