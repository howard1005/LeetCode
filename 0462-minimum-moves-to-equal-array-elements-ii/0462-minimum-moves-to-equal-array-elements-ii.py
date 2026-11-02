class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        sn = sorted(nums)
        idx = int((len(sn)-1)/2)
        avg = 0
        if len(sn) % 2 == 0:
            avg = int((sn[idx] + sn[idx+1])/2)
        else:
            avg = sn[idx]
        return sum([abs(n-avg) for n in sn])