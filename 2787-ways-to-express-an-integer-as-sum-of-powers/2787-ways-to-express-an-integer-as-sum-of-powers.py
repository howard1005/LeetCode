
MOD = 1_000_000_007

@cache
def dfs(i,r,x):
    if r == 0:
        return 1

    ret = 0

    for j in range(i,r+1):
        nr = r - j**x
        if nr >= 0:
            ret += dfs(j+1,nr,x)
            ret %= MOD
        else:
            break
    
    return ret

class Solution:

    def numberOfWays(self, n: int, x: int) -> int:
        ans = 0

        ans = dfs(1,n,x)


        return ans
