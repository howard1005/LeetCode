class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans = []
        
        cums = [nums[0]]
        for n in nums[1:]:
            cums.append(cums[-1]+n)
        
        for i in range(len(nums)):
            r = (i+1)*nums[i]-cums[i] + (cums[-1]-cums[i])-((len(nums)-(i+1))*nums[i])
            ans.append(r)
            
        return ans