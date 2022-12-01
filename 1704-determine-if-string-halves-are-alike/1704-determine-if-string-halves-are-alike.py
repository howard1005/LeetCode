class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        cnt = 0
        for i in range(0,len(s)//2):
            if s[i] in vowels:
                cnt += 1
        for i in range(len(s)//2,len(s)):
            if s[i] in vowels:
                cnt -= 1
        return cnt == 0 