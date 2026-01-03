class Solution:
    def numOfWays(self, n: int) -> int:
        ans = 0

        MOD = 1_000_000_007

        @cache
        def dfs(i,j,pt):
            # print(i,j,pt)
            if i >= n:
                return 1
            
            ret = 0

            for c in range(3):
                if pt and j>0 and pt[-1] == c:
                    continue
                if pt and j<len(pt) and pt[j] == c:
                    continue
                if j == 2:
                    ni = i+1
                    nj = 0
                    npt = pt+(c,)
                    ret += dfs(ni,nj,npt[-3:])
                else:
                    ni = i
                    nj = j+1
                    npt = pt+(c,)
                    ret += dfs(ni,nj,npt)
                ret %= MOD
                
            return ret

        ans = dfs(0,0,tuple())



        return ans