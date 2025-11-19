class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        sd = set(nums)
        v = original
        while v in sd:
            v *= 2

        return v