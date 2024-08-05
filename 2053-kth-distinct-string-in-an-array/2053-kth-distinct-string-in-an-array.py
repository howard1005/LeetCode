class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = defaultdict(int)

        for n in arr:
            d[n] += 1

        l = []
        for n in arr:
            if d[n] == 1:
                l.append(n)

        return l[k-1] if len(l) >= k else ""
                
        