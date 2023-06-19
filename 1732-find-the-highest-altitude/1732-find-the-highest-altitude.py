class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        
        cum = 0
        for g in gain:
            cum += g
            ans = max(ans,cum)
            
        return ans