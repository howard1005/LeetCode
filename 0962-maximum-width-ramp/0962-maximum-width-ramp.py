class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ans = 0

        l = [(n,i) for i,n in enumerate(nums)]
        l.sort()
        mni = l[0][1]
        for n,i in l:
            ans = max(ans,i-mni)
            mni = min(mni,i)

        return ans