class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # i:1
        d = {}
        for r in range(n+1):
            if r <= limit:
                d[r] = r+1
            elif r <= 2*limit:
                d[r] = 2*limit-r+1 
            else:
                d[r] = 0

        ans = 0

        for cnt in range(min(n+1,limit+1)):
            r = n-cnt
            ans += d[r]

        return ans