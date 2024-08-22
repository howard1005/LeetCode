class Solution:
    def findComplement(self, num: int) -> int:
        def getMsb(n):
            n |= n >> 1
            n |= n >> 2
            n |= n >> 4
            n |= n >> 8
            n |= n >> 16
            n = n + 1
            return (n >> 1)

        return ((getMsb(num)<<1)-1)^num