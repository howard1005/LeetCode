class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo,hi = 0,len(nums)-1
        while lo<=hi:
            mi = (lo+hi)//2
            if nums[mi] < target:
                lo = mi+1
            elif nums[mi] > target:
                hi = mi-1
            else:
                return mi
        return -1