class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ans = 0
        mx = max(nums)
        for n in nums:
            ans += mx-n
        return ans