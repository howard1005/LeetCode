class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        ans = 0

        n = len(nums)

        t = 0
        f = 0
        for i in range(n):
            t += nums[i]
            f += i*nums[i]
        ans = f

        for i in range(1,n):
            f += nums[i-1]*(n-1)-(t-nums[i-1])
            ans = max(ans,f)

        return ans