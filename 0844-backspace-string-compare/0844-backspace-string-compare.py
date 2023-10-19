class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def converter(s):
            st = []
            for c in s:
                if c == '#':
                    if st:
                        st.pop()
                else:
                    st.append(c)
            return ''.join(st)
        return converter(s)==converter(t)