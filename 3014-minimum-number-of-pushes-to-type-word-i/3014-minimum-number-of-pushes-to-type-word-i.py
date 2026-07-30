class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0

        d = defaultdict(int)
        for c in word:
            d[c] += 1

        l = list(d.values())
        l.sort(reverse=True)

        f = 0
        for cnt in l:
            ans += cnt*(f//8+1)
            f += 1
        
        return ans
        
        
        