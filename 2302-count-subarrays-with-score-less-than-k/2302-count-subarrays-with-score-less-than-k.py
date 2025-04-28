class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        
        i = 0
        cum = 0
        for j,n in enumerate(nums):
            cum += n
            while i<j and cum*(j-i+1) >= k:
                cum -= nums[i]
                i += 1
            if cum*(j-i+1) < k:
                ans += j-i+1

        return ans