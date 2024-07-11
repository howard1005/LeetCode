class Solution:
    def reverseParentheses(self, s: str) -> str:
        def dfs(i):
            ret = ''
            while i<len(s) and s[i]!=')':
                if s[i]=='(':
                    rs,i = dfs(i+1)
                    # print("rs",rs)
                    ret += rs
                else:
                    ret += s[i]
                    i += 1
            # print("ret",ret)
            return ''.join(reversed(ret)),i+1
        ans = ''
        i = 0
        while i<len(s) and s[i]!=')':
            if s[i]=='(':
                rs,i = dfs(i+1)
                ans += rs
            else:
                ans += s[i]
                i += 1
        return ans
            
