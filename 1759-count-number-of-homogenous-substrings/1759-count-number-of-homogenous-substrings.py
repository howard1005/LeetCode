class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 0
        
        MOD = 1000000007
        
        prev = ''
        cnt = 0
        for c in s:
            if prev == c:
                cnt += 1
            else:
                ans += cnt*(cnt+1)//2
                ans %= MOD
                cnt = 1
            prev = c
        ans += cnt*(cnt+1)//2
        ans %= MOD
        
        return ans