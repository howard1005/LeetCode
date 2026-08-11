class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]+1 == nums[i]:
                ans += nums[i]
            else:
                break

        sd = set(nums)
        while ans in sd:
            ans += 1
        
        return ans
        