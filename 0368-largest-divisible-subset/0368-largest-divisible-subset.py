from functools import reduce

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        l = [[1,-1] for _ in range(len(nums))]
        nums.sort()
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[j]%nums[i]==0:
                    if l[i][0] < l[j][0]+1:
                        l[i][0] = l[j][0]+1
                        l[i][1] = j
        ans = []
        i = l.index(max(l))
        while 1:
            ans.append(nums[i])
            i = l[i][1]
            if i == -1:
                break
        return ans