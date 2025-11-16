class Solution:
    def numSub(self, s: str) -> int:
        ans = 0

        MOD = 1_000_000_007

        l = s.split('0')
        for ss in l:
            cnt = len(ss)
            ans += cnt*(cnt+1)//2
            ans %= MOD

        return ans