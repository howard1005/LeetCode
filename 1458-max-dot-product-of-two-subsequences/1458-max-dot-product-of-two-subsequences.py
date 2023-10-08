class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        ans = -inf
        
        if len(nums1) < len(nums2):
            nums1,nums2 = nums2,nums1
        
        for n1 in nums1:
            for n2 in nums2:
                ans = max(ans,n1*n2)
                
        l = []
        for i in range(len(nums2)):
            pm = [[],[]]
            for j in range(i,len(nums2)):
                n = nums2[j]
                if n > 0:
                    if not pm[0]:
                        pm[0].append((j,n))
                    else:
                        if pm[0][-1][1] < n:
                            pm[0].append((j,n))
                elif n < 0:
                    if not pm[1]:
                        pm[1].append((j,n))
                    else:
                        if pm[1][-1][1] > n:
                            pm[1].append((j,n))
            l.append(pm)
        
        dp = [[-inf for _ in range(len(nums2))] for _ in range(len(nums1))]
        
        def dfs(i,j):
            if i >= len(nums1):
                return 0
            if j >= len(nums2):
                return 0
            
            if dp[i][j] != -inf:
                return dp[i][j]
            
            dp[i][j] = dfs(i+1,j)
            
            n1 = nums1[i]
            
            cl = []
            if n1 > 0:
                cl = l[j][0]
            if n1 < 0:
                cl = l[j][1]
                
            for k,n2 in cl:
                dp[i][j] = max(dp[i][j],n1*n2+dfs(i+1,k+1))
            
            # for k in range(j,len(nums2)):
            #     dp[i][j] = max(dp[i][j],nums1[i]*nums2[k]+dfs(i+1,k+1))

            return dp[i][j]
        
        _ans = dfs(0,0)
        
        # for r in dp:
        #     print(r)
        
        if _ans != 0:
            ans = max(ans,_ans)
        return ans