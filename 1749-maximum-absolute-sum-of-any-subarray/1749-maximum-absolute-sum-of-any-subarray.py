class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = -inf

        mn,mx = inf,-inf
        cum = 0
        for n in nums:
            cum += n
            ans = max(ans,abs(cum-min(0,mn)),abs(cum-max(0,mx)))
            mn,mx = min(mn,cum),max(mx,cum)

        return ans