class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m = max(nums)
        if m != len(nums)-1:
            return False

        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        
        for i in range(1,m):
            if d[i] != 1:
                return False
        if d[m] != 2:
            return False
        
        return True