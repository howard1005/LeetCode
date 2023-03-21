class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0 
        
        cnt = 0
        for n in nums:
            if n == 0:
                ans += cnt + 1
                cnt += 1
            else:
                cnt = 0
                
        return ans