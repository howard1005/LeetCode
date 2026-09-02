class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd,even = 0,0

        for n in nums1:
            if n%2:
                odd += 1
            else:
                even += 1
            if odd >= 2:
                return True
            if odd >=1 and even >= 1:
                return True

        if odd == 0 or even == 0:
            return True
        
        return False 