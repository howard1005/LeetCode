class Solution:
    def countElements(self, nums: List[int]) -> int:
        return sum([1 if max(nums) > n and n > min(nums) else 0 for n in nums])