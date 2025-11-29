class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cum = sum(nums)
        return cum-cum//k*k