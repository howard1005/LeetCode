class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [nums[i//2] if i&1==0 else nums[i//2+n] for i in range(2*n)]