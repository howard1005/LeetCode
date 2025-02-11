class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        st = []
        
        size = len(part)

        for c in s:
            st.append(c)
            if len(st) >= size and part == ''.join(st[-size:]):
                for _ in range(size):
                    st.pop()
        if len(st) >= size and part == ''.join(st[-size:]):
                for _ in range(size):
                    st.pop()

        return ''.join(st)
                