class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        ans = []

        for i,n in enumerate(nums):
            ans.append(nums[(i+n+len(nums))%len(nums)])
                
        return ans