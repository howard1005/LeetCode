class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ans = []
        
        l = [1]

        for i in range(1,len(nums)):
            if (nums[i-1]&1) == (nums[i]&1):
                l.append(1)
            else:
                l.append(l[-1]+1)

        for a,b in queries:
            ans.append(l[b] >= b-a+1)

        return ans