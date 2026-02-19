class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0

        f = -1
        cnt0,cnt1 = 0,0
        for c in s:
            if c == '0':
                if f == 0:
                    cnt0 += 1
                else:
                    ans += min(cnt0,cnt1)
                    f = 0
                    cnt0 = 1
            else:
                if f == 1:
                    cnt1 += 1
                else:
                    ans += min(cnt0,cnt1)
                    f = 1
                    cnt1 = 1
        ans += min(cnt0,cnt1)
                
        return ans