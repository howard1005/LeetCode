class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = 0

        ormx = 0
        for n in nums:
            ormx |= n
        
        def dfs(i,orn):
            nonlocal ans
            if i == len(nums):
                if orn == ormx:
                    ans += 1
                return
            
            dfs(i+1,orn)
            dfs(i+1,orn|nums[i])

        dfs(0,0)

        return ans