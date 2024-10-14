from heapq import heappush,heappop

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0

        h = []
        for n in nums:
            heappush(h,-n)

        while k:
            nn = heappop(h)
            n = -nn

            ans += n
            heappush(h, -(n//3+1) if n%3 else -(n//3))

            k -= 1

        return ans