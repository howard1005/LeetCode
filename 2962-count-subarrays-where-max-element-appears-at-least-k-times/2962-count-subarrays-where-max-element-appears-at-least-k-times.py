class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        
        tn = max(nums)
        cnt = 0
        i = 0
        for j,n in enumerate(nums):
            if n == tn:
                cnt += 1
            while i<j:
                if nums[i] == tn:
                    if cnt <= k:
                        break
                    cnt -= 1
                i += 1
            if cnt >= k:
                ans += i+1

        return ans