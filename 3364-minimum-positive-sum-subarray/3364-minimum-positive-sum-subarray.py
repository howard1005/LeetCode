class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = inf
        for size in range(l,r+1):
            for i in range(len(nums)-size+1):
                t = sum(nums[i:i+size])
                if t > 0:
                    ans = min(ans,t)
        return ans if ans != inf else -1