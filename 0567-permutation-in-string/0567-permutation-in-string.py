from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = defaultdict(int)
        cnt = 0
        for c in s1:
            d[c] += 1
            cnt += 1
        h,t = 0,0
        while h < len(s2):
            c = s2[h]
            d[c] -= 1
            cnt -= 1 
            while d[c]<0:
                d[s2[t]] += 1
                cnt += 1
                t += 1
            h += 1
            if cnt == 0:
                return True
        return False
            