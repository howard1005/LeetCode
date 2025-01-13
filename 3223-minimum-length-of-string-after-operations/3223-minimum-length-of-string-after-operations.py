class Solution:
    def minimumLength(self, s: str) -> int:
        ans = 0
        
        d = defaultdict(int)

        for c in s:
            d[c] += 1

        for c,cnt in d.items():
            if cnt&1:
                ans += 1
            else:
                ans += 2
        
        return ans