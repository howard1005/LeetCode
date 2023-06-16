from math import comb

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        
        MOD = 1000000007
        
        def dfs(l):
            if not l:
                return 1
            v = l[0]
            ll,rl = [],[]
            for vv in l[1:]:
                if v < vv:
                    rl.append(vv)
                else:
                    ll.append(vv)
            return (comb(len(l)-1,len(ll))*dfs(ll)*dfs(rl)) % MOD
        
        return dfs(nums)-1