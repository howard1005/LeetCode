class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        
        r = 0
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        for k,v in d.items():
            if v&1:
                ans += v-1
                r |= 1
            else:
                ans += v
        
        return ans+r
             
        