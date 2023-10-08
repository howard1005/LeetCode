class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        ans = -inf
        
        for n1 in nums1:
            for n2 in nums2:
                ans = max(ans,n1*n2)
                
        dp = [[-inf for _ in range(len(nums2))] for _ in range(len(nums1))]
        
        def dfs(i,j):
            if i >= len(nums1):
                return 0
            if j >= len(nums2):
                return 0
            
            if dp[i][j] != -inf:
                return dp[i][j]
            
            dp[i][j] = max(nums1[i]*nums2[j] + dfs(i+1,j+1),dfs(i,j+1),dfs(i+1,j))

            return dp[i][j]
        
        _ans = dfs(0,0)
        
        if _ans != 0:
            ans = max(ans,_ans)
        return ans