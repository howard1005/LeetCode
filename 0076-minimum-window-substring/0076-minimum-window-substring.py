from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = defaultdict(int)
        for c in t:
            d[c] += 1
        cnt = len(t)
        ans = float('inf') 
        ansi,ansj = 0,-1
        i = 0
        for j in range(len(s)):
            if s[j] in d:
                if d[s[j]] > 0:
                    cnt -= 1
                d[s[j]] -= 1
            while i < j:
                if s[i] not in d:
                    i += 1
                elif d[s[i]] < 0:
                    d[s[i]] += 1
                    #cnt += 1
                    i += 1
                else:
                    break
            if cnt <= 0:
                if ans > (j-i)+1:
                    ans = (j-i)+1
                    ansi,ansj = i,j
        return s[ansi:ansj+1]