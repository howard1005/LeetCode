class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        l = list(s)
        l.sort()
        return ''.join(list(sorted(l[:-1],reverse=True)))+'1'