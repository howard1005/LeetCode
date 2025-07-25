class Solution:
    def maxSum(self, nums: List[int]) -> int:
        sd = set()
        mxn = -inf
        for n in nums:
            if n > 0:
                sd.add(n)
            else:
                mxn = max(mxn,n)

        if not sd:
            return mxn
        
        return sum(sd)