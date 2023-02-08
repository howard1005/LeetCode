class Solution:
    def jump(self, nums: List[int]) -> int:
        _len = len(nums)
        mx = 0
        mxi = 0
        while mxi < _len - 1:
            _mxi = 0
            for i in range(mxi+1):
                _mxi = max(_mxi,nums[i]+i)
            mx += 1
            mxi = _mxi

        return mx
        