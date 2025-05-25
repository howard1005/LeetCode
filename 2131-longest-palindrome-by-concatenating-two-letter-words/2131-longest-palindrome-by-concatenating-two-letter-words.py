from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        
        d = defaultdict(int)
        for w in words:
            rw = w[::-1]
            if d[rw]:
                d[rw] -= 1
                ans += 4
            else:
                d[w] += 1
        
        for w,cnt in d.items():
            if cnt and w[0] == w[1]:
                ans += 2
                break
            
        return ans