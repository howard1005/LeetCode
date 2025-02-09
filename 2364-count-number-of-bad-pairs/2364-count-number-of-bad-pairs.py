class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        ans = 0
        
        d = defaultdict(int)

        for i,n in enumerate(nums):
            d[i-n] += 1

        for cnt in d.values():
            ans += (len(nums)-cnt)*cnt

        return ans//2