class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sd = set(nums)
        mn = min(sd)
        if mn < k:
            return -1
        if mn == k:
            return len(sd)-1
        return len(sd)
        
