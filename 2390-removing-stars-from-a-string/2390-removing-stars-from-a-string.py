class Solution:
    def removeStars(self, s: str) -> str:
        l = ['']*len(s)
        i = 0
        for c in s:
            if c == '*':
                i -= 1
            else:
                l[i] = c
                i += 1
        return ''.join(l[:i])