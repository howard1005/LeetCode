class Solution:
    def minimumDeletions(self, s: str) -> int:
        if len(s) == 1:
            return 0

        ans = inf

        acnt = s.count('a')
        if acnt == 0:
            return 0
        ans = acnt
        bcnt = 0

        for c in s:
            if c == 'a':
                acnt -= 1
            else:
                bcnt += 1
            ans = min(ans,acnt+bcnt)
        

        return ans