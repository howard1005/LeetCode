class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 1_000_000_007

        ans = 0

        @cache
        def dfs(i,j,t):
            if j == n:
                return 1

            ret = 0
            
            for c in range(3):
                if c == t[i]:
                    continue
                if i and c == t[i-1]:
                    continue
                nt = t[:i] + (c,) + t[i+1:]
                ni,nj = i,j
                if i == m-1:
                    ni = 0
                    nj += 1
                else:
                    ni += 1
                
                ret += dfs(ni,nj,nt)
                ret %= MOD

            return ret
            
        ans = dfs(0,0,tuple(-1 for _ in range(m)))

        return ans

        