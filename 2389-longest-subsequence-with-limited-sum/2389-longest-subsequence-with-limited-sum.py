from bisect import bisect_right


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        
        nums.sort()
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        for q in queries:
            ans.append(bisect_right(nums,q))
        
        return ans