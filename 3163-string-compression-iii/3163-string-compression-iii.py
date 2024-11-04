class Solution:
    def compressedString(self, word: str) -> str:
        ans = ''

        cnt = 0
        prev = ''
        for c in word:
            if prev == c:
                if cnt == 9:
                    ans += '9'+c
                    cnt = 0
                cnt += 1
            else:
                if cnt:
                    ans += str(cnt)+prev
                cnt = 1
                prev = c
        ans += str(cnt)+prev

        return ans