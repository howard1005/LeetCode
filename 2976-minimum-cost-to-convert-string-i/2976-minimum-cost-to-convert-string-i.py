class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        ans = 0

        def nord(c):
            return ord(c)-ord('a')

        mp = [[inf for _ in range(27)] for _ in range(27)]

        for i in range(27):
            mp[i][i] = 0

        for ac,bc,c in zip(original,changed,cost):
            a,b = nord(ac),nord(bc)
            mp[a][b] = min(mp[a][b],c)

        for k in range(27):
            for i in range(27):
                for j in range(27):
                    mp[i][j] = min(mp[i][j],mp[i][k]+mp[k][j])

        for ac,bc in zip(source,target):
            a,b = nord(ac),nord(bc)
            c = mp[a][b]
            if c == inf:
                return -1
            ans += c

        return ans