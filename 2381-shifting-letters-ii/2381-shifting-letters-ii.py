class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ans = ''

        l = [0 for _ in range(len(s))]

        for a,b,c in shifts:
            d = 1 if c == 1 else -1
            l[a] += d
            if b != len(s)-1:
                l[b+1] -= d
        
        for i in range(1,len(s)):
            l[i] += l[i-1]

        for a,c in zip(l,s):
            n = ord(c)-ord('a')
            d = (a%26+26)%26
            nn = (n+d)%26
            b = chr(nn+ord('a'))
            ans += b

        return ans