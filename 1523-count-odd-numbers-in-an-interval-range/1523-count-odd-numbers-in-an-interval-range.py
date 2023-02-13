class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans = 0
        
        diff = high-low
        if low&1:
            ans += diff//2 + 1
        else:
            ans += diff//2 + (1 if diff%2 else 0)
            
        return ans    