class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        
        cum = 1
        i,j = 0,0
        while j<len(nums):
            cum *= nums[j]
            while i<j and cum >= k:
                cum //= nums[i]
                i += 1
            if cum < k:
                ans += j-i+1
            j+=1
                
        return ans