class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        
        st = []

        for c in expression:
            if c == ')':
                tl = []
                while st and st[-1] != '(':
                    t = st.pop()
                    tl.append(t)
                st.pop()
                op = st.pop()

                if op == '!':
                    st.append(not tl[0])
                if op == '&':
                    st.append(all(tl))
                if op == '|':
                    st.append(any(tl))
            elif c == 't':
                st.append(True)
            elif c == 'f':
                st.append(False)
            elif c == ',':
                pass
            else:
                st.append(c)

        return st[0]