class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        l = []
        while n:
            l.append(n&1)
            n>>=1
        l.reverse()
        cnt = -1
        for b in l:
            if b == 0:
                cnt += 1
            else:
                ans = max(ans,cnt+1)
                cnt = 0
        return ans