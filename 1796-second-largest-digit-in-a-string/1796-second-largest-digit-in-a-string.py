class Solution:
    def secondHighest(self, s: str) -> int:
        d = {}
        for c in s:
            if c.isdigit():
                d[int(c)] = 1
        l = list(d.keys())
        l.sort(reverse=True)
        if len(l) < 2:
            return -1
        return l[1]