class Solution:
    def mirrorDistance(self, n: int) -> int:
        ans = inf

        l = list(str(n))
        l.reverse()
        rn = int(''.join(l))
        ans = abs(n-rn)
            

        return ans if ans != inf else -1