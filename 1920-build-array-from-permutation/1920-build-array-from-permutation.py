class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [-1 for _ in range(len(nums))]

        for i,n in enumerate(nums):
            ans[i] = nums[n]

        return ans