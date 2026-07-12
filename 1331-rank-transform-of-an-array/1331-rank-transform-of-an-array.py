class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ans = [0 for _ in range(len(arr))]

        d = defaultdict(list)
        for i,v in enumerate(arr):
            d[v].append(i)

        r = 1
        for v in sorted(list(d.keys())):
            l = d[v]
            for i in l:
                ans[i] = r
            r += 1
            
        return ans