class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        p,c = 0,0
        for n in nums:
            if n > 0:
                p+=1
            if n < 0:
                c+=1
        return max(p,c)