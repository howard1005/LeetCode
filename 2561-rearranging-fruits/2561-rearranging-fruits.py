class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        ans = 0

        d1 = defaultdict(int)
        d2 = defaultdict(int)

        mn = inf

        for b in basket1:
            d1[b] += 1
            mn = min(mn,b)

        for b in basket2:
            d2[b] += 1
            mn = min(mn,b)

        # print(d1,d2)

        l = []
        for b in set(d1.keys())|set(d2.keys()):
            cum = d1[b]+d2[b]
            if cum%2:
                return -1
            t = cum//2 - min(d1[b],d2[b])
            l.extend([b]*t)

        l.sort()
        # print(l)

        for i in range(len(l)//2):
            if l[i] < mn*2:
                ans += l[i]
            else:
                ans += mn*2
        
        return ans