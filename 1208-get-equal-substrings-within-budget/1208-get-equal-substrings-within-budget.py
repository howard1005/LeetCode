class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans = 0

        def getCost(c1,c2):
            return abs(ord(c1)-ord(c2))

        cost = 0
        i = 0
        for j in range(len(s)):
            cost += getCost(s[j],t[j])
            while i <= j and cost > maxCost:
                cost -= getCost(s[i],t[i])
                i += 1
            ans = max(ans,j-i+1)
            
        return ans
        