class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        for _,cnt in d.items():
            if cnt&1:
                return False
        return True