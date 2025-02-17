class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def is_ca(j):
            return True if j+1<len(p) and p[j+1] == '*' else False

        @cache
        def dfs(i,j):
            if i >= len(s) and j >= len(p):
                return True
            if i < len(s) and j >= len(p):
                return False
            if i >= len(s) and j < len(p):
                while j<len(p) and is_ca(j):
                    j += 2
                if j == len(p):
                    return True
                return False
            ca = is_ca(j)
            if ca:
                if dfs(i,j+2):
                    return True
                for k in range(i,len(s)):
                    if p[j] == '.':
                        pass
                    elif s[k] != p[j]:
                        break
                    if dfs(k+1,j+2):
                        return True
            else:
                if p[j] == '.':
                    pass
                elif s[i] != p[j]:
                    return False
                if dfs(i+1,j+1):
                    return True
            return False

        return dfs(0,0)