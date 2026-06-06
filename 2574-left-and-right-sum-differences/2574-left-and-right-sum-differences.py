class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans = []

        tot = sum(nums)
        cum = 0
        for n in nums:
            ans.append(abs(tot-n-cum-cum))
            cum += n
            

        return ans