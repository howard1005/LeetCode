class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        ans = -1
        
        nums.sort()
        
        cum = 0
        for n in nums:
            if n < cum:
                ans = cum + n
            cum += n
        
        return ans