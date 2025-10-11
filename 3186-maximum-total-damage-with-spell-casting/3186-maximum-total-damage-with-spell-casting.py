class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        ans = 0

        d = defaultdict(int)

        for p in power:
            d[p] += 1

        l = [(p,cnt) for p,cnt in d.items()]
        l.sort()

        @cache
        def dfs(i):
            if i >= len(l):
                return 0
            ret = l[i][0]*l[i][1]

            ret = max(ret,dfs(i+1))
            for j in range(i+1,i+4):
                if j<len(l) and l[j][0] > l[i][0]+2:
                    ret = max(ret,l[i][0]*l[i][1]+dfs(j))


            return ret

        ans = dfs(0)

        return ans