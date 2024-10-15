class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        
        cum = 0
        for c in s:
            if c == '1':
                cum += 1
            else:
                ans += cum
                
        return ans
        