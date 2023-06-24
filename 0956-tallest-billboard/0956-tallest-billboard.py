class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        ans = 0
        
        dp2 = {}
        def dfs2(i,a,b):
            nonlocal ans
            if i == len(rods):
                return 0 if a == b else -inf

            k2 = (i,a-b)
            if k2 in dp2:
                return dp2[k2]
            dp2[k2] = -inf
            
            ret = dfs2(i+1,a+rods[i],b) # 준것의 높은것을 기준으로 얼마나 높아 졌나
            if ret != -inf:
                base = max(a+rods[i],b) # 준것의 높은것
                dp2[k2] = max(dp2[k2],base + ret - max(a,b)) # 받은것의 높은것을 기준으로 얼마나 높아졌는지 계산
            
            
            ret = dfs2(i+1,a,b+rods[i])
            if ret != -inf:
                base = max(a,b+rods[i])
                dp2[k2] = max(dp2[k2],base + ret - max(a,b))
            
            
            ret = dfs2(i+1,a,b)
            if ret != -inf:
                base = max(a,b)
                dp2[k2] = max(dp2[k2],base + ret - max(a,b))
            
            return dp2[k2]
            
        ans = dfs2(0,0,0)
              
        return ans
                