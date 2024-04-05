class Solution:
    def makeGood(self, s: str) -> str:
        st = []
        for c in s:
            if st and st[-1] == c.swapcase():
                st.pop()
            else:
                st.append(c)
        
        return ''.join(st)