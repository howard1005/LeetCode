class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1,len(s)):
            if len(s) % i == 0:
                if s[:i]*(len(s)//i) == s:
                    return True
        return False