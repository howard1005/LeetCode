class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        
        mx = max(nums)
        cnt = 0
        i,j = 0,0
        while j < len(nums):
            if nums[j] == mx:
                cnt += 1
            while cnt >= k:
                if nums[i] == mx:
                    cnt -= 1
                i += 1
            ans += i
            j += 1
            
        return ans
            