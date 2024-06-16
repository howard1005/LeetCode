class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        u = 1
        i = 0
        ans = 0
        while u <= n:
            if i < len(nums) and nums[i] <= u:
                u += nums[i]
                i += 1
            else:
                u *= 2
                ans += 1
        return ans