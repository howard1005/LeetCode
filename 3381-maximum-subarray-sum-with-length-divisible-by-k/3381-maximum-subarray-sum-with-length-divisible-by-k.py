class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        ans = -inf

        d = defaultdict(lambda:inf)
        d[k-1] = 0

        cum = 0
        for i,n in enumerate(nums):
            cum += n
            m = i%k

            ans = max(ans,cum-d[m])

            d[m] = min(d[m],cum)
            

        return ans