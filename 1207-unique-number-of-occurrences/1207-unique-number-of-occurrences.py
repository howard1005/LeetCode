from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = defaultdict(int)
        for n in arr:
            d[n] += 1
        od = {}
        for o in d.values():
            if o in od:
                return False
            od[o] = 1
        return True