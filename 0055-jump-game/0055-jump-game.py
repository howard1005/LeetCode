class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        vis = [0 for _ in range(len(nums))]
        n = 0
        for i in range(len(nums)-1):
            if nums[i]:
                n += 1
                j = i+nums[i]
                if j < len(nums):
                    vis[i+nums[i]] -= 1
            n += vis[i]
            if n == 0:
                return False
        return True
            