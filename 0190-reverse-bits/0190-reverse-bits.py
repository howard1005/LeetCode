class Solution:
    def reverseBits(self, n: int) -> int:
        l = []
        while n:
            l.append(n&1)
            n >>= 1
        l += [0]*(31-len(l))
        ans = 0
        for b in l:
            ans += b
            ans <<= 1
        return ans