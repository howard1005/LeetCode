class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0

        for e in (15,12,9,6,3):
            k = 10**e
            cnt = n-k+1
            if cnt > 0:
                ans += cnt

        return ans