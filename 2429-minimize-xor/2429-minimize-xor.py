class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def countBit(n):
            ret = 0
            while n:
                ret += n&1
                n >>= 1
            return ret

        ans = 0

        cnt = countBit(num2)

        for i in range(32,-1,-1):
            b = (1<<i)
            if cnt and b&num1:
                ans |= b
                cnt -= 1

        for i in range(33):
            b = (1<<i)
            if cnt and b&ans==0:
                ans |= b
                cnt -= 1

        return ans