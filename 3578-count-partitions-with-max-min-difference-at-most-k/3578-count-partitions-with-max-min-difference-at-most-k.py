from sortedcontainers import SortedList

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        ans = 0

        MOD = 1_000_000_007

        sl = SortedList()

        dp = [0 for _ in range(len(nums))]

        i,j = 0,0

        while j < len(nums):
            sl.add(nums[j])

            while k < sl[-1]-sl[0]:
                sl.remove(nums[i])
                i += 1
            if i == 0:
                dp[j] += 1
            dp[j] += (dp[j-1] if j-1>=0 else 0)-(dp[i-2] if i-2>=0 else 0)
            if j-1>=0:
                dp[j] += dp[j-1]
            dp[j] %= MOD

            j += 1
        # print(dp)

        ans = (dp[-1]-dp[-2]+MOD)%MOD

        return ans