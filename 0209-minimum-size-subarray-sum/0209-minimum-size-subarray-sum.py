class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = inf
        
        i,j = 0,0
        cum = 0
        while i<len(nums) or j<len(nums):
            if cum < target:
                if j == len(nums):
                    break
                cum += nums[j]
                j += 1
                
            else:
                if cum - nums[i] >= target:
                    if i == j:
                        break
                    cum -= nums[i]
                    i += 1
                    
                else:
                    if j == len(nums):
                        break
                    cum += nums[j]
                    j += 1
            if cum >= target:
                ans = min(ans,j-i)

                
        return 0 if ans == inf else ans