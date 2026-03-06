class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        f = 1
        for c in s:
            if c == '1':
                if f:
                    pass
                else:
                    return False
            else:
                f = 0
        return True
                
        