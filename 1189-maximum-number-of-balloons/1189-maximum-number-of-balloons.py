class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {c:0 for c in 'balloon'}
        for c in text:
            if c in d:
                d[c] += 1
        d['l'] //= 2
        d['o'] //= 2
        return min(list(d.values()))
            
            