class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            ss = ''
            for i in range(len(s)-1):
                n = (int(s[i])+int(s[i+1]))%10
                ss += str(n)
            s = ss
        return s[0] == s[1]
                