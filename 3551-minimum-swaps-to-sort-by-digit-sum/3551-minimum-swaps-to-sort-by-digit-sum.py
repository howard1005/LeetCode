class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ans = 0

        l = [(i,n,sum([int(c) for c in str(n)])) for i,n in enumerate(nums)]
        l.sort(key=lambda x: (x[2],x[1]))
        # print(l)

        d = {}
        for i,t in enumerate(l):
            d[t[0]] = i

        vis = set()
        for i in range(len(nums)):
            if i in vis and i == d[i]:
                continue
            
            size = 0

            j = i
            while j not in vis:
                vis.add(j)
                size += 1
                j = d[j] 
            if size > 0:
                ans += size-1

        return ans