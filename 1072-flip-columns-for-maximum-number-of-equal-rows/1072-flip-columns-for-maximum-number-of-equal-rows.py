class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        d = defaultdict(int)

        for r in matrix:
            t = tuple(r)
            d[t] += 1
            rt = tuple([n^1 for n in r])
            d[rt] += 1
        
        return max(d.values())