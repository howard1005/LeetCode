class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vs = ('a','e','i','o','u')
        for c in s:
            if c in vs:
                return True
        return False

        