class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        def chk_cap(s):
            for c in s:
                if ord(c) < ord('A') or ord('Z') < ord(c):
                    return False
            return True
        def chk_ncap(s):
            for c in s:
                if ord(c) < ord('a') or ord('z') < ord(c):
                    return False
            return True
        
        if chk_cap(word[0]):
            return chk_cap(word[1:]) or chk_ncap(word[1:])
        else:
            return chk_ncap(word[1:])
        