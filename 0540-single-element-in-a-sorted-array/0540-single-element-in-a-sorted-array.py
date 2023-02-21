class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ans = 0
        lo,hi = 0,len(nums)-1
        while lo<=hi:
            mi = (lo+hi)//2
            if mi&1:
                if nums[mi]==nums[mi-1]:
                    lo = mi+1
                else:
                    hi = mi-1
                    ans = nums[mi-1]
            else:
                if mi and nums[mi]==nums[mi-1]:
                    hi = mi-1
                else:
                    lo = mi+1
                    ans = nums[mi]
        return ans
                    