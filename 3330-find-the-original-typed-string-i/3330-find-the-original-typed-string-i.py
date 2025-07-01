class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1
        
        prev = ''
        cnt = 1

        for c in word:
            if prev == c:
                cnt += 1
            else:
                ans += cnt-1
                prev = c
                cnt = 1
        ans += cnt-1

        return ans