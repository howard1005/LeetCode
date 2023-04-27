class Solution:
    def bulbSwitch(self, n: int) -> int:
        ans = 0
        
        m = 1
        while m * m <= n:
            ans += 1
            m += 1
            
        return ans