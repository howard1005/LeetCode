class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0

        def dfs(i,t):
            if i == len(nums):
                nonlocal ans
                ans += t
                return
            dfs(i+1,t)
            dfs(i+1,t^nums[i])
        dfs(0,0)

        return ans