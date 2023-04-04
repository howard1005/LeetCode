class Solution:
    def partitionString(self, s: str) -> int:
        ans = 0
        
        d = {}
        for c in s:
            if c in d:
                ans += 1
                d = {}
            d[c] = 1
        if d:
            ans += 1
        
        return ans