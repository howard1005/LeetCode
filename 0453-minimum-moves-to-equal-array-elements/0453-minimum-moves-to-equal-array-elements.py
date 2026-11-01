class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mn = min(nums)
        
        ans = 0

        for n in nums:
            ans += n-mn

        return ans