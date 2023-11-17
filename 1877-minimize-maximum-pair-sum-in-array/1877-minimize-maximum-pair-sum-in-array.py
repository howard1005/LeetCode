class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        ans = 0
        
        nums.sort()
        for i in range(len(nums)//2):
            ans = max(ans,nums[i] + nums[-1-i])
            
        return ans