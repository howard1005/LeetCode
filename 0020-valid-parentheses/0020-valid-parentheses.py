class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')', '{':'}', '[':']'}
        st = []
        for c in s:
            if c in '({[':
                st.append(d[c])
            else:
                if not st:
                    return False
                if st[-1] != c:
                    return False
                st.pop()
        if st:
            return False
        return True
        

            