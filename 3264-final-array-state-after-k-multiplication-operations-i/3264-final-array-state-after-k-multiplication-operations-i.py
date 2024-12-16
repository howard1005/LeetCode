from heapq import heappush,heappop

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        ans = nums[:]

        hq = []

        for i,n in enumerate(nums):
            heappush(hq,(n,i))
        
        while k:
            n,i = heappop(hq)
            n *= multiplier
            ans[i] = n
            heappush(hq,(n,i))
            k -= 1

        return ans