class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans = nums[0]

        l = sorted(nums[1:])
        
        ans += l[0]+l[1]

        return ans