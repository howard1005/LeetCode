class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        def getMsb(n):
            n |= n >> 1
            n |= n >> 2
            n |= n >> 4
            n |= n >> 8
            n |= n >> 16
            n = n + 1
            return (n >> 1)

        return ((getMsb(n)<<1)-1)^n