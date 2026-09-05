class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        l = [0 for _ in range(len(nums))]
        l[0] = nums[0]
        rl = [0 for _ in range(len(nums))]
        rl[-1] = nums[-1]

        for i in range(1,len(nums)):
            l[i] = max(l[i-1],nums[i])

        for i in range(len(nums)-2,-1,-1):
            rl[i] = min(rl[i+1],nums[i])

        for i in range(len(nums)):
            if l[i]-rl[i] <= k:
                return i

        return -1

        