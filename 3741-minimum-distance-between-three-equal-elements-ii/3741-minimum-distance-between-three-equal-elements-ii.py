class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        ans = inf

        d = defaultdict(list)

        for i,n in enumerate(nums):
            d[n].append(i)

        for l in d.values():
            if len(l) >= 3:
                for i in range(len(l)-2):
                    ans = min(ans,2*(l[i+2]-l[i]))
                    
        return ans if ans != inf else -1