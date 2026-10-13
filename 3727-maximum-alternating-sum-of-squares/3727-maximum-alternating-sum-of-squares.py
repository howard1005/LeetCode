class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        ans = 0

        nums.sort(key=lambda x:abs(x))

        mi = len(nums)//2
        for i in range(mi):
            n = nums[i]
            ans -= n*n

        for i in range(mi,len(nums)):
            n = nums[i]
            ans += n*n

        return ans