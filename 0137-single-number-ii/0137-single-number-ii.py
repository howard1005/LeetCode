class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        for k,v in d.items():
            if v == 1:
                return k
        return -1