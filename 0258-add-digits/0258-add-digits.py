class Solution:
    def addDigits(self, num: int) -> int:
        def dfs(n):
            t = 0
            while n:
                t += n%10
                n //= 10
            return t
        while num >= 10:
            num = dfs(num)
        return num