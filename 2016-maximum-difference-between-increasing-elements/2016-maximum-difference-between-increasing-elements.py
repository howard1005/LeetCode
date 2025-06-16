class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -inf

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    ans = max(ans,-nums[i]+nums[j])

        return ans if ans != -inf else -1