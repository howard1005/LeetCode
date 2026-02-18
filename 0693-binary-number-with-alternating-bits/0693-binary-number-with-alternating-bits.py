class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = format(n,'b')

        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                return False
        
        return True