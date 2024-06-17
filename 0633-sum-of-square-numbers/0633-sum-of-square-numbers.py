class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        d = {}
        i = 0
        while i*i <= c:
            d[i*i] = 1
            if c - i*i in d:
                return True
            i += 1
        return False