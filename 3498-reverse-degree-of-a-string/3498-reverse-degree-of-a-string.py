class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for i,c in enumerate(s):
            n = ord(c)-ord('a')
            n = 26-n
            ans += n*(i+1)

        return ans