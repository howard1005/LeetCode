
from heapq import heappush, heappop

class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)

        # 1. Dual Heap + Sliding Window
        low = []   # Max Heap
        high = []  # Min Heap

        side = [0] * n
        sum_low = sum_high = 0
        size_low = size_high = 0

        def clean():
            while low and low[0][1] < left:
                heappop(low)
            while high and high[0][1] < left:
                heappop(high)

        def balance():
            nonlocal sum_low, sum_high, size_low, size_high

            clean()

            while size_low > size_high + 1:
                v, i = heappop(low)
                v = -v

                sum_low -= v
                size_low -= 1

                heappush(high, (v, i))
                side[i] = 1
                sum_high += v
                size_high += 1
                clean()

            while size_low < size_high:
                v, i = heappop(high)

                sum_high -= v
                size_high -= 1

                heappush(low, (-v, i))
                side[i] = 0
                sum_low += v
                size_low += 1
                clean()

        costs = []
        left = 0

        for right, v in enumerate(nums):
            clean()

            if not low or v <= -low[0][0]:
                heappush(low, (-v, right))
                sum_low += v
                size_low += 1
                side[right] = 0
            else:
                heappush(high, (v, right))
                sum_high += v
                size_high += 1
                side[right] = 1

            # 윈도우에서 이전 원소 제거
            if right >= x:
                old = nums[left]

                if side[left] == 0:
                    sum_low -= old
                    size_low -= 1
                else:
                    sum_high -= old
                    size_high -= 1

                left += 1

            balance()

            if right >= x - 1:
                med = -low[0][0]

                cost = (
                    med * size_low - sum_low
                    + sum_high - med * size_high
                )
                costs.append(cost)

        # 2. DP: 겹치지 않는 구간 k개 선택
        INF = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            dp = [INF] * (n + 1)

            for i in range(x, n + 1):
                dp[i] = min(
                    dp[i - 1],
                    prev[i - x] + costs[i - x]
                )

            prev = dp

        return prev[n]
