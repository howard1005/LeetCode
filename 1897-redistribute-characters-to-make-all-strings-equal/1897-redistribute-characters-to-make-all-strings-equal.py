class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = defaultdict(int)
        for w in words:
            for c in w:
                d[c] += 1
        
        for k,v in d.items():
            if v % len(words) != 0:
                return False
        
        return True