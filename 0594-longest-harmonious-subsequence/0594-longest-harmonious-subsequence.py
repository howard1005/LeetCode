class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ans = 0

        d = defaultdict(int)

        for n in nums:
            d[n] += 1
        
        for k,cnt in d.items():
            if k in d and k+1 in d:
                ans = max(ans,d[k]+d[k+1])

        return ans
        