class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans = 0
        
        tot = sum(nums)

        cum = 0
        for n in nums[:-1]:
            cum += n
            if cum >= tot-cum:
                ans += 1
        
        return ans