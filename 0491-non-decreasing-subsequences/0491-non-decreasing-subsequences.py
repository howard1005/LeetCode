class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        def dfs(i,p,l):
            if i >= len(nums):
                if 2 <= len(l):
                    ans.add(tuple(l))
                return
            if nums[i] >= p:
                dfs(i+1,nums[i],l+[nums[i]])
            dfs(i+1,p,l)
        dfs(0,-101,[])
        
        return ans