class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token == '/':
                n1,n2 = st.pop(), st.pop()
                st.append(int(n2/n1))
            elif token == '+':
                n1,n2 = st.pop(), st.pop()
                st.append(n2+n1)
            elif token == '-':
                n1,n2 = st.pop(), st.pop()
                st.append(n2-n1)
            elif token == '*':
                n1,n2 = st.pop(), st.pop()
                st.append(n2*n1)
            else:
                st.append(int(token))
        return st.pop()