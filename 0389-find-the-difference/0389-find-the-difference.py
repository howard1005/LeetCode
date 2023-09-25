from collections import defaultdict

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        for c in t:
            d[c] -= 1
            if d[c] == -1:
                return c