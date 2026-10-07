class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        cand = []

        def dfs(i,o,r,p):
            if i == len(s):
                if o == 0:
                    cand.append((p,r))
                return

            c = s[i]
            if c == '(':
                dfs(i+1,o+1,r,p+c)
                dfs(i+1,o,r+1,p)
            elif c == ')':
                if o > 0:
                    dfs(i+1,o-1,r,p+c)
                dfs(i+1,o,r+1,p)
            else:
                dfs(i+1,o,r,p+c)

        dfs(0,0,0,'')

        ans = []

        cand.sort(key=lambda x:x[1])
        mn = cand[0][1]
        for i in range(len(cand)):
            if cand[i][1] > mn:
                break
            ans.append(cand[i][0])

        sd = set(ans)
        ans = list(sd)

        return ans
                
            