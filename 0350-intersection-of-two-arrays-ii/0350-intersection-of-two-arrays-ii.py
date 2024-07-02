class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        d = {}

        for n in nums1:
            if n not in d:
                d[n] = [1,0]
            else:
                d[n][0] += 1

        for n in nums2:
            if n in d:
                d[n][1] += 1
        
        for n,l in d.items():
            ans += [n] * min(l)

        return ans