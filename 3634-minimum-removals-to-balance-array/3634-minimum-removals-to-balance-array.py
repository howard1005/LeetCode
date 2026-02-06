from bisect import bisect_right

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        ans = len(nums)-1

        nums.sort()
        for i,n in enumerate(nums):
            j = bisect_right(nums,n*k)
            ans = min(ans,i+len(nums)-j)

        return ans    