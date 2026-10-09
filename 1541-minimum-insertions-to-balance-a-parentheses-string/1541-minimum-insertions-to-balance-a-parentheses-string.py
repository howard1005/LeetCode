class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0

        cnt = 0
        for c in s:
            if c == '(':
                if cnt&1:
                    cnt -= 1
                    ans += 1
                cnt += 2
            else:
                if cnt == 0:
                    cnt += 2
                    ans += 1
                cnt -= 1

        ans += cnt
                
        return ans