class Solution:
    def kthCharacter(self, k: int) -> str:
        w = 'a'

        while len(w) < k:
            for c in w[:]:
                n = ord(c)-ord('a')
                n = (n+1)%26
                nc = chr(n+ord('a'))
                w += nc

        return w[k-1]