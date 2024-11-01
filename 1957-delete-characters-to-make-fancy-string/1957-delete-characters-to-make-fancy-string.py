class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = ''

        cnt = 0
        prev = ''
        for c in s:
            if c == prev:
                if cnt < 2:
                    cnt += 1
                    ans += c
            else:
                prev = c
                cnt = 1
                ans += c

        return ans
        