class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0

        MOD = 1000000007

        def bit_size(a):
            ret = 0
            while a:
                ret += 1
                a >>= 1
            return ret

        for a in range(1,n+1):
            ans <<= bit_size(a)
            ans |= a
            ans %= MOD

        return ans