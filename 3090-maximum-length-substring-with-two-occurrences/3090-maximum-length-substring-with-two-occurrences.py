class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0

        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                d = defaultdict(int)
                f = True
                for c in s[i:j]:
                    d[c] += 1
                    if d[c]>2:
                        f = False
                        break
                if f:
                    ans = max(ans,j-i)

        return ans

                