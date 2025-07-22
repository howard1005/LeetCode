class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        vis = [0 for _ in range(10001)]
        ans = 0
        sum = 0
        j = 0
        for i in range(len(nums)):
            while vis[nums[i]]:
                vis[nums[j]] = 0
                sum -= nums[j]
                j += 1
            vis[nums[i]] = 1
            sum += nums[i]
            ans = max(ans,sum)
        return ans
                    