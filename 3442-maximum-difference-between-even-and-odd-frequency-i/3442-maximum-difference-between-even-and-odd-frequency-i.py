class Solution:
    def maxDifference(self, s: str) -> int:
        d = defaultdict(int)

        for c in s:
            d[c] += 1
        
        l = list(d.values())
        
        a1,a2 = -1,inf

        for n in l:
            if n&1:
                a1 = max(a1,n)
            else:
                a2 = min(a2,n)

        return a1-a2