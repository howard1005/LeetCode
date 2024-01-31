class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        l = [int(c) for c in str(n)]
        l.reverse()
        
        ans = 1000000000000
        
        def dfs(i,a):
            nonlocal ans
            if i == len(l):
                if sum([int(c) for c in str(n+a)]) <= target:
                    ans = min(ans,a)
                return
            
            dfs(i+1,a)
            
            e = 10**i if i!=0 else 1
            up = 10-(n+a)//e%10
            if up != 10:
                dfs(i+1,up*e+a)

        dfs(0,0)
        
        return ans
            