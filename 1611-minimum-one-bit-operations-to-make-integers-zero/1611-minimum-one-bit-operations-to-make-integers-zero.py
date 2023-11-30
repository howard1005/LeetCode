class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0
        
        l = []
        while n:
            l.append(n&1)
            n >>= 1
            
        dp1 = [1]
        for i in range(1,len(l)):
            dp1.append(dp1[-1]*2+1)
        
        dp2 = [-1 for _ in range(len(l))]
        
        def dfs(i):
            if i == 0:
                return 1
            if i < 0:
                return 0
            
            if dp2[i] != -1:
                return dp2[i]
            dp2[i] = 0
            
            if l[i-1] == 0:
                dp2[i] = dfs(i-1) + 1 + dp1[i-1]
            else:
                j = i-2
                while j >= 0:
                    if l[j] == 1:
                        break
                    j -= 1
                dp2[i] = dfs(j) + 1 + dp1[i-1]
                
            return dp2[i]
                   
        ans = dfs(len(l)-1)
        
        return ans