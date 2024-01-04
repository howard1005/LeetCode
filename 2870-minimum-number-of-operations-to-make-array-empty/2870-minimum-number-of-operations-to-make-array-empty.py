class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        
        d = defaultdict(int)
        
        for n in nums:
            d[n] += 1
            
        for v in d.values():
            if v == 1:
                return -1
            ans += v//3 + (1 if v%3 else 0)
            
        return ans
            