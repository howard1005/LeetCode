class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while 1:
            p = 1
            for c in str(n):
                p *= int(c)
            if p%t == 0:
                return n
            n += 1