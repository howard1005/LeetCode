class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        ans = inf

        pd = defaultdict(set)
        ed = defaultdict(set)

        for a,b in edges:
            ed[a].add(b)
            ed[b].add(a)

        xord = {}

        def dfs(par,i,ps):
            pd[i] |= ps
            v = nums[i]
            ps.add(i)
            for j in ed[i]:
                if j == par:
                    continue
                v ^= dfs(i,j,ps)
            ps.remove(i)
            xord[i] = v
            return v
            
        dfs(-1,0,set())

        # print(xord)
        # print(pd)

        def subtree(i,j):
            return i in pd[j]

        for i in range(1,len(nums)):
            for j in range(i+1,len(nums)):
                if subtree(i,j):
                    a = xord[0]^xord[i]
                    b = xord[i]^xord[j]
                    c = xord[j]
                if subtree(j,i):
                    a = xord[0]^xord[j]
                    b = xord[j]^xord[i]
                    c = xord[i]
                if not subtree(i,j) and not subtree(j,i):
                    a = xord[0]^xord[i]^xord[j]
                    b = xord[i]
                    c = xord[j]
                diff = max(a,b,c) - min(a,b,c)
                ans = min(ans,diff)
                

        return ans