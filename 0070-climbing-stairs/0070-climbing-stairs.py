class Solution:
    def climbStairs(self, n: int) -> int:
        l = [0 for _ in range(n)]
        l[0] = 1
        if n > 1:
            l[1] = 1
        for i in range(n):
            if i+1 < n:
                l[i+1] += l[i]
            if i+2 < n:
                l[i+2] += l[i]
        return l[-1]
