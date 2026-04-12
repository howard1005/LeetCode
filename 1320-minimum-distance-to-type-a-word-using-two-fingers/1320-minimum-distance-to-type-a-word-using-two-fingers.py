class Solution:
    def minimumDistance(self, word: str) -> int:
        ans = -1

        r,c = 5,6

        def distance(a,b):
            if a == -1:
                return 0
            y1,x1 = a//c,a%c
            y2,x2 = b//c,b%c
            return abs(y1-y2) + abs(x1-x2)

        @cache
        def dfs(i,a,b):
            if i == len(word):
                return 0
            ret = inf
            ch = word[i]
            cn = ord(ch)-ord('A')
            dis1 = distance(a,cn)
            ret = min(ret,dfs(i+1,cn,b)+dis1)
            dis2 = distance(b,cn)
            ret = min(ret,dfs(i+1,a,cn)+dis2)
            return ret

        ans = dfs(0,-1,-1)

        return ans