class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        slen = len(s)
        zl = [0 for _ in range(slen)]
        ol = [0 for _ in range(slen)]
        for i in range(slen):
            zl[i] += (s[i] == '0')
            ol[i] += (s[i] == '1')
            if i:
                zl[i] += zl[i-1]
                ol[i] += ol[i-1]
        ans = zl[-1]
        for i in range(slen):
            ans = min(ans, ol[i] + zl[-1] - zl[i])
            
        return ans
