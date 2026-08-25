class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        sd = set(nums)

        i = k
        while i in sd:
            i += k

        return i 