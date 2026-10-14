class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        ans = ''
        k = sum
        for _ in range(num):
            m = min(9,k)
            ans += str(m)
            k -= m
        return ans if k == 0 else ""
            