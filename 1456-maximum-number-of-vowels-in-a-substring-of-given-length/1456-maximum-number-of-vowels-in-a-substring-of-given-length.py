class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        
        v = {'a','e','i','o','u'}
        
        cnt = 0
        for i in range(k):
            if s[i] in v:
                cnt += 1
        ans = cnt
        
        for i in range(k,len(s)):
            if s[i-k] in v:
                cnt -= 1
            if s[i] in v:
                cnt += 1
            ans = max(ans,cnt)
             
        return ans