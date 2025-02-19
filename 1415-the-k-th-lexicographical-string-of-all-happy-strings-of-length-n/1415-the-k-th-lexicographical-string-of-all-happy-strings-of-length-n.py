class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = ''
        cnt = 0
        def dfs(s):
            if len(s) == n:
                nonlocal ans,cnt
                cnt += 1
                if cnt == k:
                    ans = s
                    return True
                return False
                
            for c in 'abc':
                if s == '':
                    if dfs(s+c):
                        return True
                elif s[-1] != c:
                    if dfs(s+c):
                        return True
        dfs('')
        return ans