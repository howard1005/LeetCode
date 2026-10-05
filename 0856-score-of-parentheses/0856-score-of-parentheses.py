class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = [0]
        for c in s:
            if c == '(':
                st.append(0)
            else:
                v = st.pop()
                if v == 0:
                    st[-1] += 1
                else:
                    st[-1] += 2*v
        return st[0]
                
                