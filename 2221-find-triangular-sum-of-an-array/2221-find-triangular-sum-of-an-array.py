class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        l = nums
        while len(l) > 1:
            nl = []
            for i in range(len(l)-1):
                nl.append((l[i]+l[i+1])%10)
            l = nl
        return l[0]