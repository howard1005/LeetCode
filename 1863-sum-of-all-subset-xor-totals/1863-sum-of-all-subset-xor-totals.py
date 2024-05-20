class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0

        def dfs(i,x):
            nonlocal ans
            if i == len(nums):
                ans += x
                return
            dfs(i+1,x)
            dfs(i+1,x^nums[i])
        dfs(0,0)

        return ans