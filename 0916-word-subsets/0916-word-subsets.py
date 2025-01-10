from collections import defaultdict

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def s2d(s):
            d = defaultdict(int)
            for c in s:
                d[c] += 1
            return d
        
        gd = defaultdict(int)
        for s in words2:
            d = s2d(s)
            for k in d:
                gd[k] = max(gd[k], d[k])
        
        ans = []
        for s in words1:
            d = s2d(s)
            flag = 1
            for k in gd:
                if gd[k] > d[k]:
                    flag = 0
                    break
            if flag:
                ans.append(s)
        return ans