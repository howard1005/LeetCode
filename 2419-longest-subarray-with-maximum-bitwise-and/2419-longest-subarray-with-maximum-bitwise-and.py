class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0

        k = max(nums)

        cnt = 0
        for n in nums:
            if n == k:
                cnt += 1
            else:
                cnt = 0
            ans = max(ans,cnt)

        return ans