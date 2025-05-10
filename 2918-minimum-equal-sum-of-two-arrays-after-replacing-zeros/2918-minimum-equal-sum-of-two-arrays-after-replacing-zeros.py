class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        t1,t2 = 0,0
        z1,z2 = 0,0

        for n in nums1:
            if n == 0:
                z1 = 1
                t1 += 1
            else:
                t1 += n

        for n in nums2:
            if n == 0:
                z2 = 1
                t2 += 1
            else:
                t2 += n

        ans = -1

        if z1 and z2:
            ans = max(t1,t2)
        elif z1:
            if t1 > t2:
                ans = -1
            else:
                ans = t2
        elif z2:
            if t1 < t2:
                ans = -1
            else:
                ans = t1
        else:
            if t1 == t2:
                ans = t1
        
        return ans
                
            