class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = defaultdict(int)
        
        for n in nums:
            d[n] += 1
            
        mx = max(d.values())
        
        return sum(map(lambda x: x if x==mx else 0, d.values()))
                