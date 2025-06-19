class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        ans = 1

        nums.sort()

        h = nums[0]

        for i,n in enumerate(nums):
            if n-h>k:
                ans += 1
                h = n

        return ans