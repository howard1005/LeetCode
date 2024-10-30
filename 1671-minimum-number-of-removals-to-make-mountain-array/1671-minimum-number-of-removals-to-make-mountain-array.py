class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        
        dp = {}

        def dfs(i,j,k):
            if i == len(nums):
                if k != 2:
                    return inf
                return 0
            
            if (i,j,k) in dp:
                return dp[(i,j,k)]
            dp[(i,j,k)] = inf

            dp[(i,j,k)] = min(dp[(i,j,k)],dfs(i+1,j,k)+1)
            if j == -1 or (k == 0 and nums[j] < nums[i]) or (k >= 1 and nums[j] > nums[i]):
                kk = 2 if k == 1 else k
                dp[(i,j,k)] = min(dp[(i,j,k)],dfs(i+1,i,kk))
                if j != -1 and i < len(nums)-1 and k == 0:
                    dp[(i,j,k)] = min(dp[(i,j,k)],dfs(i+1,i,1))
            
            return dp[(i,j,k)]
                    
        return dfs(0,-1,0)