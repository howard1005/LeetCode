class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        def proc(l1,l2):
            for c1,c2 in zip(l1,l2):
                if c1 > c2:
                    return False
            return True
        l1,l2 = sorted(list(s1)),sorted(list(s2))
        return proc(l1,l2) or proc(l2,l1)