class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        it = set(nums1) & set(nums2)
        return min(it) if it else -1