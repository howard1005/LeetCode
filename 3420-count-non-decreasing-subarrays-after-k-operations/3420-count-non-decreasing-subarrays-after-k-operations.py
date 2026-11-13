class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dq = deque()
        cost = ans = 0
        r = n - 1

        for l in range(n - 1, -1, -1):
            while dq and nums[dq[0]] < nums[l]:
                i = dq.popleft()
                j = dq[0] if dq else r + 1
                cost += (nums[l] - nums[i]) * (j - i)

            dq.appendleft(l)

            while cost > k:
                cost -= nums[dq[-1]] - nums[r]
                if dq[-1] == r:
                    dq.pop()
                r -= 1

            ans += r - l + 1

        return ans
