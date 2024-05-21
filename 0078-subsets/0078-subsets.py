class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(i,l):
            if i == len(nums):
                ans.append(l)
                return
            dfs(i+1,l)
            dfs(i+1,l+[nums[i]])
        dfs(0,[])

        return ans