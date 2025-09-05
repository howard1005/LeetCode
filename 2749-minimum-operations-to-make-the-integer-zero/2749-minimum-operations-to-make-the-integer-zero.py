class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        ans = -1

        for k in range(1,61):
            t = num1 - num2*k
            if t < 0:
                break
            cnt = t.bit_count()
            if t >= k and cnt <= k:
                ans = k
                break



        return ans
        