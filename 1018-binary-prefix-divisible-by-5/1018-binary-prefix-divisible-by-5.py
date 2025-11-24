class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        
        m = 0
        for n in nums:
            m = (m<<1)|n
            m %= 5
            if m == 0:
                ans.append(True)
            else:
                ans.append(False)

        return ans