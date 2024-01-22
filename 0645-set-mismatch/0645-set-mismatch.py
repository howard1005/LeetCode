from collections import defaultdict

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = [-1,-1]
        
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        for i in range(1,len(nums)+1):
            if i not in d:
                ans[1] = i
            if d[i] == 2:
                ans[0] = i
        
        return ans