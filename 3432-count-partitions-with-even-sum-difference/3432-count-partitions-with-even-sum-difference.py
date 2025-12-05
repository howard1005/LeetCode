class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        ans = 0
        tot = sum(nums)
        cum = 0
        for n in nums[:-1]:
            cum += n
            if (tot-2*cum)%2 == 0:
                ans += 1
        return ans