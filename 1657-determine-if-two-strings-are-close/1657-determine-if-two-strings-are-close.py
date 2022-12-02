from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1,d2 = defaultdict(int),defaultdict(int)
        for c in word1:
            d1[c] += 1
        for c in word2:
            d2[c] += 1
        return len(word1)==len(word2) and set(d1.keys())==set(d2.keys()) and sorted(d1.values())==sorted(d2.values())