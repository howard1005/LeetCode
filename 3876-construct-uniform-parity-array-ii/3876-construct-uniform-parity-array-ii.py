class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd,even = 0,0

        omn = inf

        for n in nums1:
            if n%2:
                odd += 1
                omn = min(omn,n)
            else:
                even += 1
            
        if odd == 0 or even == 0:
            return True

        of,ef = True,True

        for n in nums1:
            if n%2:
                if n <= omn:
                    ef = False
            else:
                if n <= omn:
                    of = False
        
        return ef or of