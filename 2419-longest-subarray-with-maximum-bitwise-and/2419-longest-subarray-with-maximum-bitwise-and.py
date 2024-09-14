class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 1
        
        mx = max(nums)

        cnt = 0
        for n in nums:
            if n == mx:
                cnt += 1
            else:
                cnt = 0
            ans = max(ans,cnt)

        return ans