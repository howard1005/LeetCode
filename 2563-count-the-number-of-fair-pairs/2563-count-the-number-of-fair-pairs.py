from bisect import bisect_left,bisect_right

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0

        nums.sort()
        
        for i,n in enumerate(nums):
            ii = bisect_left(nums, lower-n,i+1,len(nums))
            jj = bisect_right(nums, upper-n,i+1,len(nums))
            ans += jj-ii

        return ans