class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        ans = -1

        @cache
        def dfs(i):
            if i == len(nums)-1:
                return 0
            ret = -1
            a = nums[i]
            for j in range(i+1,len(nums)):
                b = nums[j]
                if abs(a-b) <= target:
                    v = dfs(j)
                    if v != -1:
                        ret = max(ret,v+1)
            # print(i,ret)
            return ret

        ans = dfs(0)

        return ans