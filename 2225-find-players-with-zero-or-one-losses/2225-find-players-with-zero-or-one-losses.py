from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = [[],[]]
        
        d = defaultdict(lambda:[0,0])
        for w,l in matches:
            d[w][0] += 1
            d[l][1] += 1
        for i,(w,l) in d.items():
            if l in [0,1]:
                ans[l].append(i)
        ans[0].sort()
        ans[1].sort()
        
        return ans