from collections import defaultdict

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        d1 = defaultdict(int)
        for n in target:
            d1[n] += 1
        d2 = defaultdict(int)
        for n in arr:
            d2[n] += 1
        if len(d1) != len(d2):
            return False
        for n in d1:
            if d1[n] != d2[n]:
                return False
        return True
            