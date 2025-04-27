class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-2):
            a,b,c = nums[i:i+3]
            if 2*(a+c) == b:
                ans += 1
        return ans