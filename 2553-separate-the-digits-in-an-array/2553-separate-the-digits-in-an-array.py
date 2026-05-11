class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        l = []
        for n in nums:
            for c in str(n):
                l.append(int(c))
        return l
            