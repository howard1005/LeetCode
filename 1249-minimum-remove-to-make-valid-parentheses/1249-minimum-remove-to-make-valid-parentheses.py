class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        d = {}
        st = []
        for i,c in enumerate(s):
            if c == '(':
                st.append(i)
            elif c == ')':
                if st:
                    st.pop()
                else:
                    d[i] = 1
        while st:
            d[st.pop()] = 1
        ans = ''
        for i,c in enumerate(s):
            if i not in d:
                ans += c
        return ans