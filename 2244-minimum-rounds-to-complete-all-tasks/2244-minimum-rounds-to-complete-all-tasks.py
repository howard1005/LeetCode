from collections import defaultdict

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        ans = 0
        
        d = defaultdict(int)
        for t in tasks:
            d[t] += 1
        for v in d.values():
            if v == 1:
                return -1
            ans += v//3 + (1 if v%3 else 0)
        
        return ans