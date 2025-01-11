class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        d = defaultdict(int)
        for c in s:
            d[c] += 1

        o = 0
        r = 0
        for _,cnt in d.items():
            o += cnt//2
            r += cnt&1

        if r > k:
            return False

        if 2*o < k-r:
            return False

        return True
