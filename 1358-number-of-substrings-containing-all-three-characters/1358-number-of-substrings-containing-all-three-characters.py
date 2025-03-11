class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0

        d = defaultdict(int)

        i = 0
        for c in s:
            d[c] += 1
            while len(d) == 3:
                rc = s[i]
                if d[rc] == 1:
                    break
                d[rc] -= 1
                i += 1
            if len(d) == 3:
                ans += i+1

        return ans
            