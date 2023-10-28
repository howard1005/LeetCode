class Solution:
    def countVowelPermutation(self, n: int) -> int:
        d = {}
        def dfs(i,c):
            if i == n:
                return 1
            if (i,c) in d:
                return d[(i,c)]
            ret = 0
            if c == 'a':
                ret += dfs(i+1,'e')
            elif c == 'e':
                ret += dfs(i+1,'a') + dfs(i+1,'i')
            elif c == 'i':
                ret += dfs(i+1,'a') + dfs(i+1,'e') + dfs(i+1,'o') + dfs(i+1,'u')
            elif c == 'o':
                ret += dfs(i+1,'i') + dfs(i+1,'u')
            elif c == 'u':
                ret += dfs(i+1,'a')
            else:
                ret += dfs(i+1,'a') + dfs(i+1,'e') + dfs(i+1,'i') + dfs(i+1,'o') + dfs(i+1,'u')
            ret %= 1000000007
            d[(i,c)] = ret
            return ret
        return dfs(0,'')
                    