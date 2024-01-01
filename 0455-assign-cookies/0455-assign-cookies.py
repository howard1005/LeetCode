class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ans = 0
        
        g.sort()
        s.sort()
        
        i,j = 0,0
        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                ans += 1
                i += 1
                j += 1
            else:
                j += 1
        
        return ans
        