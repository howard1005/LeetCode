class Solution:
    def robotWithString(self, s: str) -> str:
        ansl = []

        d = defaultdict(int)
        
        for i,c in enumerate(s):
            d[c] = i

        st = []

        i = 0

        for tc in 'abcdefghijklmnopqrstuvwxyz':
            while st and st[-1] <= tc:
                ansl.append(st.pop())
            while i < len(s) and i <= d[tc]:
                st.append(s[i])
                while st and st[-1] <= tc:
                    ansl.append(st.pop())
                i += 1

        while st:
            ansl.append(st.pop())

        return ''.join(ansl)