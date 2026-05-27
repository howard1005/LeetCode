class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0

        d = {}

        for i,c in enumerate(word):
            if ord('a') <= ord(c) and ord(c) <= ord('z'):
                d[c] = i
            if ord('A') <= ord(c) and ord(c) <= ord('Z'):
                if c not in d:
                    d[c] = i
        
        for n,N in zip(range(ord('a'),ord('z')+1),range(ord('A'),ord('Z')+1)):
            c,C = chr(n),chr(N)
            if c in d and C in d and d[c]<d[C]:
                ans += 1

        return ans

        
