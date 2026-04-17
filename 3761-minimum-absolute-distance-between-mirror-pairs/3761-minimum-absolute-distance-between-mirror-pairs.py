from bisect import bisect_left

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        ans = inf

        d = defaultdict(list)
        for i,n in enumerate(nums):
            l = list(str(n))
            l.reverse()
            rn = int(''.join(l))
            d[rn].append(i)

        # print(d)

        for j,n in enumerate(nums):
            l = d[n]
            if not l:
                continue
            i = bisect_left(l,j)
            # print(i,j,n,l)
            if i-1>=0:
                ans = min(ans,abs(l[i-1]-j))
            

        return ans if ans != inf else -1