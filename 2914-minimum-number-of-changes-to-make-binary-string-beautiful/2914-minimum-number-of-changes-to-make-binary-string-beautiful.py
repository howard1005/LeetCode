class Solution:
    def minChanges(self, s: str) -> int:
        ans = 0
        
        for i in range(0,len(s),2):
            cc = s[i:i+2]
            if cc not in ['00','11']:
                ans += 1

        return ans