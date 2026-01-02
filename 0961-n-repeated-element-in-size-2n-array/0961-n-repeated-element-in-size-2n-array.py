class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        n = len(nums)//2
        
        d = defaultdict(int)

        for v in nums:
            d[v] += 1
            if d[v] == n:
                return v

        return None
        
