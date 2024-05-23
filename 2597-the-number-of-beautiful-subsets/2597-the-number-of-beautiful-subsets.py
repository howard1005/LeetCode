class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        ans = 0

        def dfs(i,d):
            nonlocal ans

            if i == len(nums):
                ans += 1
                return

            dfs(i+1,d)

            n = nums[i]
            if n not in d:
                dfs(i+1,{n-k,n+k} | d)

        dfs(0,set())

        return ans-1