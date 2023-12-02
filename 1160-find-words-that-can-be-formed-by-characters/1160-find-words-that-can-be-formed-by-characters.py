class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        
        def s2d(s):
            d = defaultdict(int)
            for c in s:
                d[c] += 1
            return d
        
        d = s2d(chars)
        for w in words:
            size = len(w)
            for c,cnt in s2d(w).items():
                if d[c] < cnt:
                    size = 0
                    break
            ans += size
        
        return ans