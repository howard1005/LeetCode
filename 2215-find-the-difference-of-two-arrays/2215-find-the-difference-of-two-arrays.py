class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = [set(),set()]
        
        d1 = {n:1 for n in nums1}
        d2 = {n:1 for n in nums2}
        
        for n in nums1:
            if n not in d2:
                ans[0].add(n)
                
        for n in nums2:
            if n not in d1:
                ans[1].add(n)
        
        return ans