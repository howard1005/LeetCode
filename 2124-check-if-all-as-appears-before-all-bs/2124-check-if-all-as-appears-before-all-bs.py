class Solution:
    def checkString(self, s: str) -> bool:
        f = False
        for c in s:
            if c == 'b':
                f = True
            elif f:
                return False
        return True