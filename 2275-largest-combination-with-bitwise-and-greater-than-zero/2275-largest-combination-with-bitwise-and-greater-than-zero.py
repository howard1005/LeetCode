class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        d = defaultdict(int)

        for n in candidates:
            i = 0
            while n:
                if n&1:
                    d[i] += 1
                n >>= 1
                i += 1
        
        return max(d.values())