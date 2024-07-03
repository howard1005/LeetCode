class Solution:
    def minDifference(self, nums: List[int]) -> int:
        ans = inf

        nums.sort()

        for i in range(4):
            j = 3-i
            ii = i if i<len(nums) else -1
            jj = j if j<len(nums) else len(nums)-1

            ans = min(ans,abs(nums[-jj-1]-nums[ii]))

        return ans