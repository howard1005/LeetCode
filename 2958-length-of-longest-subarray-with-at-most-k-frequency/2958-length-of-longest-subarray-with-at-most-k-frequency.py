class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        
        d = defaultdict(int)
        i,j = 0,0
        while j<len(nums):
            n = nums[j]
            d[n] += 1
            if d[n] > k:
                while d[n] > k:
                    d[nums[i]] -= 1
                    i += 1
            ans = max(ans,j-i+1)
            j += 1
            
        return ans