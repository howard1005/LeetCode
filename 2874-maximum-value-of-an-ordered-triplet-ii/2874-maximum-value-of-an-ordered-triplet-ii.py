class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        mx = -inf
        mxdiff = -inf
        for n in nums:
            ans = max(ans,mxdiff*n)
            mxdiff = max(mxdiff,mx-n)
            mx = max(mx,n)
        return ans