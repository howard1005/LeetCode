class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        ans = 0

        if sum(nums) == 0:
            return 0

        x = 0
        for n in nums:
            x ^= n
        
        ans = len(nums)

        if x == 0:
            ans -= 1

        return ans