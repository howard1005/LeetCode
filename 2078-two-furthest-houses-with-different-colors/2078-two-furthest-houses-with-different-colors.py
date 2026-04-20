class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0

        d = defaultdict(set)

        for i,c in enumerate(colors):
            d[c].add(i)

        for k,sd in d.items():
            a,b = 0,len(colors)-1
            while a in sd:
                a += 1
            while b in sd:
                b -= 1
            if a<len(colors):
                for c in sd:
                    ans = max(ans,abs(a-c))
            if b>=0:
                for c in sd:
                    ans = max(ans,abs(b-c))

        return ans