class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        
        up = 0
        for i in range(len(s)-1,0,-1):
            c = s[i]
            if c == '1':
                if up == 0:
                    ans += 1
                    up = 1
            else:
                if up:
                    ans += 1

                
        return ans + len(s) - 1 + up