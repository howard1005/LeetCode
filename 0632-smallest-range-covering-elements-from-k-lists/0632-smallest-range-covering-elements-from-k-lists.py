class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        ans = []
        
        l = []

        for i,r in enumerate(nums):
            for n in r:
                l.append((n,i))

        l.sort()
        print(l)

        mnr,mn = [],inf

        d = defaultdict(int)
        cnt = 0
        i = 0
        t = 0
        while cnt < len(nums):
            n,j = l[i]
            if d[j] == 0:
                cnt += 1
            d[j] += 1
            i += 1
            while t<i and d[l[t][1]] > 1:
                d[l[t][1]] -= 1
                t += 1
        if l[i-1][0]-l[t][0]+1 < mn:
            mn = l[i-1][0]-l[t][0]+1
            mnr = [l[t][0],l[i-1][0]]

        print(mn,mnr)
        for k in range(i,len(l)):
            n,j = l[k]
            d[j] += 1
            while t<k and d[l[t][1]] > 1:
                d[l[t][1]] -= 1
                t += 1
            if l[k][0]-l[t][0]+1 < mn:
                mn = l[k][0]-l[t][0]+1
                mnr = [l[t][0],l[k][0]]
        
        ans = mnr

        return ans